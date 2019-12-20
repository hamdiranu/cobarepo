import re
import pprint
def cekDataTransaksi(logs) :
    output={
        'nomor_seri': '94309403940394039403',
        'id_transaksi': '14879',
        'id_order':'YPSTRX-Indragiri|IDG-14879',
        'nomor_referensi': '394039403',
        'success': True
    }
    for i in logs:
        pattern = '#(\d+)'
        hasil=re.search(pattern,i)                      # id_transaksi
        if re.search(pattern,i):
            output['id_transaksi'] = hasil.group(1)
        
        pattern = 'SN:(\d+)'
        hasil=re.search(pattern,i)
        if re.search(pattern,i):
            output['nomor_seri'] = hasil.group(1)       # nomor_seri
        else :
            output['nomor_seri'] = 'None'

        pattern = 'Id. :(\d+)'
        hasil=re.search(pattern,i)
        if re.search(pattern,i):                        # nomor_referensi
            output['nomor_referensi'] = hasil.group(1)
        else :
            output['nomor_referensi'] = 'None'

        pattern = '([A-Z]+-[a-zA-Z]+\|[A-Z]+-\d+)'
        hasil=re.search(pattern,i)
        if re.search(pattern,i):                        # Id_order
            output['id_order'] = hasil.group(1)
        
        if output['nomor_seri']!='None':
            output['success']= True                     # success
        else :
            output['success']= False

    return output

'YPSTRX-Brebes|BYS-18254'


print('')

pprint.pprint(cekDataTransaksi([
    'Insert Transaction #14879',
    'Update Status To Pending Payment With Deposit',
    'Transaction Paid trx_id = YPSTRX-Indragiri|IDG-14879',
    'Transaction On Biller  type_modem arg: telkomsel_mobile queue_name arg: smtel-banyumas_mobile',
    'Success Manual SN:94309403940394039403 Ref Id. :394039403'
]))

'''
{
    'nomor_seri': '94309403940394039403',
    'id_transaksi': '14879',
    'id_order':'YPSTRX-Indragiri|IDG-14879',
    'nomor_referensi': '394039403',
    'success': True
}
'''
print('')

pprint.pprint(cekDataTransaksi([
    'Insert Transaction #18254',
    'Update Status To Pending Payment With Deposit',
    'Transaction Paid trx_id = YPSTRX-Brebes|BYS-18254',
    'Transaction On Biller  type_modem arg: telkomsel_mobile queue_name arg: smtel-banyumas_mobile',
    'Trx. Cancel Process Begin | cancel trx with id18254',
    'Sukses Refunded trx id. 18254 with Wallet hash #eko827p7rk89m456'
]))

'''
{
    'nomor_referensi': None,
    'nomor_seri': None,
    'id_transaksi': '18254',
    'id_order': 'YPSTRX-Brebes|BYS-18254',
    'success': False
}
'''
print('')