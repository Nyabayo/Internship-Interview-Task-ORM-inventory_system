# from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Product
import json

# Create your views here.

@csrf_exempt
@require_http_methods(["GET"])
def list_products(request):
    """
    Listing all the products present in my database.
    """
    try:
        products = Product.objects.all().values()
        return JsonResponse(list(products), safe=False, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


@csrf_exempt
@require_http_methods(["POST"])
def add_product(request):
    """
    Adding any new product to my database.
    """
    try:
        data = json.loads(request.body)
        # Validate required fields
        if not all(key in data for key in ["name", "description", "price", "stock"]):
            return JsonResponse({"error": "Missing required fields"}, status=400)

        # Create a new product
        product = Product.objects.create(
            name=data["name"],
            description=data["description"],
            price=data["price"],
            stock=data["stock"],
        )
        return JsonResponse(
            {"message": "Product added successfully!", "product_id": product.id},
            status=201,
        )
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON payload"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


@csrf_exempt
@require_http_methods(["PUT"])
def update_product(request, product_id):
    """
    Updating the details of an existing product in my database.
    """
    try:
        data = json.loads(request.body)
        product = Product.objects.get(id=product_id)

        # Update fields if provided
        product.name = data.get("name", product.name)
        product.description = data.get("description", product.description)
        product.price = data.get("price", product.price)
        product.stock = data.get("stock", product.stock)
        product.save()

        return JsonResponse({"message": "Product updated successfully!"}, status=200)
    except Product.DoesNotExist:
        return JsonResponse({"error": "Product not found!"}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON payload"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


@csrf_exempt
@require_http_methods(["DELETE"])
def delete_product(request, product_id):
    """
    Deleting any product by its ID.
    """
    try:
        product = Product.objects.get(id=product_id)
        product.delete()
        return JsonResponse({"message": "Product deleted successfully!"}, status=200)
    except Product.DoesNotExist:
        return JsonResponse({"error": "Product not found!"}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

