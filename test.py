        if Sellers.objects.exists(email=email):
            seller = Sellers.objects.get(email=email)
            if password == seller.password :
                return redirect(reverse('store_view'))