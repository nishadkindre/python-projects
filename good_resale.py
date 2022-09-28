
# TODO : To calculate the amount payable as per the law while selling a purchased capital good within 5 years(60 months)

def gst_(mrp, gp):
    gpp = 100 + gp
    gst = (mrp/(gpp/100))*(gp/100)
    return gst

def resale(price, gp, duration, sp):
    gst = gst_(price, gp) 
    per_month_itc = gst/60
    payable_itc = (60-duration)*per_month_itc 
    payable_gst = gst_((price-sp), gp)
    pay = max(payable_gst, payable_itc)
    print('-'*35)
    print('ITC redeemed : ',round(gst,1))
    print('ITC to be returned : ', round(payable_itc,1))
    print('GST payable on current sale : ', round(payable_gst,1))
    print('-'*35)
    print('Pay to Gov : ', round(pay,1))

print('-'*35)
price = int(input('Enter the Purchase Price : '))
gst = int(input('Enter the GST% : '))
duration = int(input('Enter the duration of Goods\' use(in months) : '))
sp = int(input('Enter the Selling Price : '))

resale(price, gst, duration, sp)

'''
Note :
. In case of resale of a capital good within a span of 5 years, a amount is charged and is payable to the Authority
  The amount is considered to be the maximum among two amounts viz.
  1.GST payable on current sale considering the same rate when goods initially purchased &
  2.Remaining ITC payable as the ITC exempt is divided along 5 years/60 months i.e Total ITC - (ITC/60)*months usage left

. In India the GST rates vary according to the category a Good/Service fall into, appropriate rates are advised to be used

. It is a fair/advisable practice to pay the gst during the resale of a capital good, negligence of which can attract scruting from the tax officials.

. Tax mandatory to pay only if sale of good within 5 years from the purchase of the Good.
'''

# Refer : https://taxguru.in/goods-and-service-tax/gst-capital-goods.html