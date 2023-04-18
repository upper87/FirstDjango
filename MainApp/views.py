from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        "name": "Nikolay",
        "email": "me_mail@mail.ru"
    }
    crumbs = breadcrumbs
    # text = """<h1>"Изучаем Django"</h1>
    #       <strong> Автор </strong> : <i> Лобанов С.А.</i>"""
    # return HttpResponse(text)
    return render(request, "index.html", context)

about_dict = {
    "name": "Иван",
    "sername":"Петрович",
    "last_name": "Иванов",
    "phone": "8-923-600-01-02",
    "email": "vasya@mail.ru"
}

def about(request):
    result = f"""
    <p> Имя: <strong> {about_dict["name"]} </strong> </p>
    <p> Отчество: <strong> {about_dict["sername"]} </strong> </p>
    <p> Фамилия: <strong> {about_dict["last_name"]} </strong> </p>
    <p> телефон: <strong> {about_dict["phone"]} </strong> </p>
    <p> email: <strong> {about_dict["email"]} </strong> </p>
    """
    return HttpResponse(result)

items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 3, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 4, "name": "Картофель фри" ,"quantity":0},
   {"id": 5, "name": "Кепка" ,"quantity":124},
]

breadcrumbs = [
    {"page": "Главная" ,"link":"/"}
]

def get_item(request, id):
    for item in items:
        if item["id"] == id:
            # res = f"""
            # <h1> Имя:{item["name"]} </h1>
            # <a href='/items'> Назад </a>
            # """
            # return HttpResponse(res)
            context = {
                "item": item
            }
            return render(request, "item.html", context)
    # print(f"{id=}, {type(id) = }")
    return HttpResponseNotFound("""<h1>Товара нету</h1>""")


def get_items(request):
    # res_items = "<h2>Список товаров</h2><ol>"
    # for item in items:
    #     res_items += f"""<li><a href="item/{item["id"]}">{item['name']}</a></li>"""
    # res_items += "</ol>"
    # return HttpResponse(res_items)
    context = {
        "items": items
    }
    return render(request, "items-list.html", context)