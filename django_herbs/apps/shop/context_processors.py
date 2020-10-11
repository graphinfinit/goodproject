from .models import Cart 

def show_basket(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    
    
    products = Cart.objects.filter(session_key = session_key)
    products_total_nmb = products.count()
    
    
    
    
    return locals()
    
    
def request(request):
    return {'request': request}