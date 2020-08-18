from django.shortcuts import render
from serviceControl.models import *
from .forms import *

# Create your views here.
def principal(request):
    dicionario=dict()

    #dados
    dicionario=_getData(dicionario)
    
    #Dados do front-end
    _getDataClient(request)
    _getDataShip(request)
    _getDataSeaport(request)
    _getDataFactory(request)
    _getDataService(request)
    return render(request, 'serviceControl/index.html', dicionario)
         
def _getData(dicionario):
    dicionario['serviceAll'] = Service.objects.all()
    dicionario['clientAll']  = Client.objects.all() 
    dicionario['shipAll']    = Ship.objects.all() 
    dicionario['factoryAll'] = Factory.objects.all() 
    dicionario['seaportAll'] = Seaport.objects.all() 
    return dicionario

def _getDataClient(request):
    name = request.POST.get('nameClient')    
    if (name==None or name=='')==False:
        Client.objects.create(name=name)
    return 0

def _getDataShip(request):
    nameShip = request.POST.get('shipName')
    imoNumber = request.POST.get('imoNumber') 
    if((nameShip==None or nameShip=='')and(imoNumber==None or imoNumber==''))==False:
        Ship.objects.create(imoNumber=imoNumber,shipName=nameShip)        
    return 0

def _getDataSeaport(request):
    nameSeaport = request.POST.get('nameSeaport')
    country = request.POST.get('country')
    if((nameSeaport==None or nameSeaport=='')and(country==None or country==''))==False:
        print(nameSeaport +"  "+country)
        Seaport.objects.create(name=nameSeaport,country=country)
    return 0

def _getDataFactory(request):
    name = request.POST.get('nameFactory')    
    if (name==None or name=='')==False:
        Factory.objects.create(name=name)
    return 0

def _getDataService(request):
    #ID's
    saida   = request.POST.get('saida')
    destino = request.POST.get('destino')
    navio   = request.POST.get('navio')
    cliente = request.POST.get('cliente')
    usina   = request.POST.get('usina')
    #values
    ordem   = request.POST.get('ordem')
    peso    = request.POST.get('peso')
    mes     = request.POST.get('mes')
    ano     = request.POST.get('ano')
    tipo    = request.POST.get('tipoS')
    #get objects
    if ( (ordem==None or ordem=='')and(peso==None or peso=='')and(mes==None or mes=='')and(ano==None or ano==''))==False:
        packing = Seaport.objects.get(id=saida)
        destiny = Seaport.objects.get(id=destino)
        factory = Factory.objects.get(id=usina)
        ship    = Ship.objects.get(id=navio)
        client  = Client.objects.get(id=cliente)
        print(client)
        print(packing)
        print(destiny)
        print(factory)
        print(ship)
        Service.objects.create(packing = packing,
                              destiny=destiny,
                              factory=factory,
                              ship=ship,
                              client=client,
                              year=ano,
                              month=mes,
                              salesOrder=ordem,
                              budgetedAmount=peso,
                              serviceType=tipo) 

    return 0     