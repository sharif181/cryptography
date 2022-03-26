import ast
from django.shortcuts import render
from core.algorithms import AES, DES, RSA, DSA
import time
from datetime import timedelta
from django.http import HttpResponse


def homepage(request):
    return render(request, 'algorithms/home.html')


def AESPageView(request):
    return render(request, 'algorithms/aes-page.html')


def AESEncryptView(request):
    try:
        start_time = time.time() * 1000
        if request.FILES:
            plain_text = request.FILES['file'].read()
            plain_text = plain_text.decode('UTF-8')
        key = request.POST.get('key')
        if not key or not plain_text:
            return HttpResponse("error")

        aes = AES.AESCipher(key=key)
        encrypted = aes.encrypt(plain_text=plain_text)
        end_time = time.time() * 1000
        context = {
            "encrypted_value": encrypted,
            'encryption_time': f'Encryption time {round(end_time - start_time, 2)} ms'
        }

        return render(request, 'algorithms/aes-page.html', context)
    except:
        return HttpResponse("please provide valid file")


def AESDecryptView(request):
    try:
        start_time = time.time() * 1000
        key = request.POST.get('key')
        encrypted_value = request.POST.get('encrypted_string')
        if not key or not encrypted_value:
            return HttpResponse("please provide all informations")
        aes = AES.AESCipher(key=key)
        decrypted = aes.decrypt(encrypted_text=encrypted_value)
        end_time = time.time() * 1000
        context = {
            "decrypted_value": decrypted,
            'decryption_time': f'Decryption time {round(end_time - start_time, 2)} ms'
        }

        return render(request, 'algorithms/aes-page.html', context)

    except:
        return HttpResponse("Invalid Key")


def DesPageView(request):
    return render(request, 'algorithms/des-page.html')


def DESEncryptView(request):
    try:
        start_time = time.time() * 1000
        if request.FILES:
            plain_text = request.FILES['file'].read()
            plain_text = plain_text.decode('UTF-8')
        key = request.POST.get('key')
        if not key or not plain_text:
            return HttpResponse("error")
        des = DES.DESCipher(secret=key)
        encrypted = des.encrypt(plain_text=plain_text)
        end_time = time.time() * 1000
        context = {
            "encrypted_value": encrypted,
            'encryption_time': f'Encryption time {round(end_time - start_time, 2)} ms'
        }

        return render(request, 'algorithms/des-page.html', context)
    except:
        return HttpResponse("invalid file")


def DESDecryptView(request):
    try:
        start_time = time.time() * 1000
        key = request.POST.get('key')
        encrypted_value = request.POST.get('encrypted_string')
        if not key or not encrypted_value:
            return HttpResponse("please provide all informations")
        des = DES.DESCipher(secret=key)
        decrypted = des.decrypt(encrypted_string=encrypted_value)
        end_time = time.time() * 1000
        context = {
            "decrypted_value": decrypted,
            'decryption_time': f'Decryption time {round(end_time - start_time, 2)} ms'
        }

        return render(request, 'algorithms/des-page.html', context)
    except:
        return HttpResponse("Invalid key")


def RSAView(request):
    return render(request, 'algorithms/rsa-page.html')


def RSAKEYView(request):
    p = 11
    q = 29
    rsa = RSA.RSACipher()
    n = rsa.get_N(p, q)
    phi_func = rsa.get_phi_of_n(p, q)
    e = rsa.get_encryption_key(n, phi_func)
    d = rsa.get_decryption_key(e, phi_func)
    # to avoid key collision
    while d == e:
        d = rsa.get_decryption_key(e, phi_func)

    public_key = [e, n]
    private_key = [d, n]

    context = {
        'public_key': public_key,
        'private_key': private_key
    }
    return render(request, 'algorithms/rsa-page.html', context)


def RSAEncrypt(request):
    try:
        start_time = time.time() * 1000
        if request.FILES:
            plain_text = request.FILES['file'].read()
            plain_text = plain_text.decode('UTF-8')
        public_key = request.POST.get('public_key')
        if not public_key or not plain_text:
            return HttpResponse("error")
        rsa = RSA.RSACipher()
        m_text = rsa.text_to_digits(plain_text)
        public_key = ast.literal_eval(public_key)
        c_text = rsa.encrypt(m_text, public_key)
        end_time = time.time() * 1000
        context = {
            "encrypted_value": c_text,
            'encryption_time': f'Encryption time {round(end_time - start_time, 2)} ms'
        }

        return render(request, 'algorithms/rsa-page.html', context)
    except:
        return render('invalid file')


def RSADecrypt(request):
    try:
        start_time = time.time() * 1000
        private_key = request.POST.get('private_key')
        encrypted_value = request.POST.get('encrypted_string')
        if not private_key or not encrypted_value:
            return HttpResponse("please provide all informations")
        encrypted_value = ast.literal_eval(encrypted_value)
        private_key = ast.literal_eval(private_key)
        rsa = RSA.RSACipher()
        d_text = rsa.decrypt(encrypted_value, private_key)
        final_text = rsa.digits_to_text(d_text)
        end_time = time.time() * 1000
        context = {
            "decrypted_value": final_text,
            'decryption_time': f'Decryption time {round(end_time - start_time, 2)} ms'
        }

        return render(request, 'algorithms/rsa-page.html', context)
    except:
        return HttpResponse("Invalid key")


def DSAView(request):
    return render(request, 'algorithms/dsa-page.html')


def DSAKEYView(request):
    dsa = DSA.DSACipher()
    encryption_key = dsa.get_encrypt_key()
    decryption_key = dsa.get_decrypt_key(encryption_key)

    context = {
        'public_key': encryption_key,
        'private_key': decryption_key
    }
    return render(request, 'algorithms/dsa-page.html', context)


def DSAEncryptView(request):
    try:
        start_time = time.time() * 1000
        if request.FILES:
            plain_text = request.FILES['file'].read()
            plain_text = plain_text.decode('UTF-8')
        public_key = request.POST.get('public_key')
        if not public_key or not plain_text:
            return HttpResponse("error")
        dsa = DSA.DSACipher()
        c_text = dsa.encrypt(int(plain_text), int(public_key))
        end_time = time.time() * 1000
        context = {
            "encrypted_value": c_text,
            'encryption_time': f'Encryption time {round(end_time - start_time, 2)} ms'
        }

        return render(request, 'algorithms/dsa-page.html', context)
    except:
        return HttpResponse("please provide valid file")


def DSADecryptView(request):
    try:
        start_time = time.time() * 1000
        private_key = request.POST.get('private_key')
        encrypted_value = request.POST.get('encrypted_string')
        if not private_key or not encrypted_value:
            return HttpResponse("please provide all informations")
        encrypted_value = int(encrypted_value)
        private_key = int(private_key)
        dsa = DSA.DSACipher()
        final_text = dsa.decrypt(encrypted_value, private_key)
        end_time = time.time() * 1000
        context = {
            "decrypted_value": final_text,
            'decryption_time': f'Decryption time {round(end_time - start_time, 2)} ms'
        }

        return render(request, 'algorithms/dsa-page.html', context)
    except:
        return HttpResponse("Invalid key")