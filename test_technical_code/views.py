from django.shortcuts import render

# Generate triangle
def generate_triangle(n):
    result = []
    for i in range(1, n+1):
        result.append(' '.join(str(x) for x in range (1, i+1)))
    return result

# Generate odd number (ganjil)
def generate_odd_number(n):
    return [x for x in range(1, n+1) if x % 2 != 0]

# Generate prime number (bilangan prima)
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_prime_number(n):
    return [x for x in range(2, n+1) if is_prime(x)]


def index():
    results = []
    if request.method == "POST":
        try:
            n = int(request.POST.get("number"))
            if "triangle" in request.POST:
                result = generate_triangle(n)
            elif "odd" in request.POST:
                result = generate_odd_number(n)
            elif "prime" in request.POST:
                result = generate_prime_number(n)
        except ValueError:
            result = ["Enter a valid number!"]
    return render(request, "test_technical_code/index.html", {"result": result})

    