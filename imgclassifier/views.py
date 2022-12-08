from django.shortcuts import render
from django.core.files.storage import default_storage
from rest_framework.response import Response
from rest_framework.views import APIView, View
from .forms import *

from .apps import InceptionConfig
import torch
from torchvision import transforms, models, datasets
from PIL import Image
import numpy



class classifyView(View):
    def get(self, request):
        form=ImageForm()
        context={
            'form':form,
        }
        return render(request,'imgclassifier/upload.html', context)
    
    def post(self, request):
        form=ImageForm(request.POST, request.FILES)
        context={}
        Images.objects.all().delete()
        if form.is_valid():
            form.save()
            
        images=Images.objects.all()
        context['image']=images
        
        res={}
        if len(images)>0:
            res=inceptionClassifier(images[0].image)
        context=context | res
        return render(request,'imgclassifier/upload.html', context)
        


def returnHome(request):
    form=ImageForm()
    context={
        'form':form,
    }
    return render(request,'imgclassifier/upload.html', context)
    
    
class uploadView(APIView):
# Create your views here.
    def get(self,request):
        # return render(request,'imgclassifier/upload.html')
        return Response({'status':'get success'},status=201)
    @torch.no_grad()
    def post(self,request):
        # return Response({'status':'post success'},status=201)
        if request.method=='POST':
            reponse={}
            device = 'cuda' if torch.cuda.is_available() else 'cpu'
            fileObj=request.data.get('file')
            file_name_1='pic.jpg'
            file_name=default_storage.save(file_name_1,fileObj)
            file_url=default_storage.url(file_name)
            try:
                img=Image.open('.'+file_url).convert('RGB')
            except IOError:
                return Response({
                    'status': 'error', 
                    'error': 'not an image file',
                    'file_name': file_name,
                    'file_url':file_url,
                    },status=400)
            
            input_size=(300,300)
        
            image_transforms = transforms.Compose(
                [
                    transforms.Resize(input_size, interpolation=transforms.InterpolationMode.BILINEAR),
                    transforms.ToTensor(), # transforms.PILToTensor()
                    transforms.Normalize((0.425,0.415,0.405),(0.205,0.205,0.205)),
                ]
            )
            tensor=image_transforms(img).unsqueeze(0).to(device)
            
            model=InceptionConfig.model
            model.eval()
            output=model(tensor)
            index=output.data.cpu().numpy().argmax()
            score=output.data.cpu().numpy().max()
            label=InceptionConfig.categories[index]
            reponse['status']='success'
            reponse['category']=label
            reponse['coeffiecient']=str(score)
            
            return Response(reponse,status=201)
        else:
            return Response({'status': 'error', 'error': 'not a POST method'},status=400)

@torch.no_grad()
def inceptionClassifier(file):
    file_name=file.name
    file_url=file.path
    response={}
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    try:
        img=Image.open(file_url).convert('RGB')
    except IOError:
        return {
            'status': 'error', 
            'error': 'not an image file',
            'file_name': file_name,
            'file_url':file_url,
            }
    
    input_size=(300,300)
        
    image_transforms = transforms.Compose(
        [
            transforms.Resize(input_size, interpolation=transforms.InterpolationMode.BILINEAR),
            transforms.ToTensor(), # transforms.PILToTensor()
            transforms.Normalize((0.425,0.415,0.405),(0.205,0.205,0.205)),
        ]
    )
    tensor=image_transforms(img).unsqueeze(0).to(device)
    
    model=InceptionConfig.model
    model.eval()
    output=model(tensor)
    index=output.data.cpu().numpy().argmax()
    score=output.data.cpu().numpy().max()
    label=InceptionConfig.categories[index]
    response['status']='success'
    response['category']=label
    response['coeffiecient']=str(score)
    
    return response
