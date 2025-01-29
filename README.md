mysql.server start

mysql -u root

python manage.py runserver

board

show databases;

python manage.py makemigrations

python manage.py migrate



def meal_list(request):
    meal = Meal.objects.all() #モデルからデータをすべて取得しmealに入れる


    total_calories = sum(meal.calories for meal in meals) 
    #for meal in meals で meals に含まれる各食事（meal）を順番に取り出し、
    #meal.calories を取得する。sum　は、それらの calories の値をすべて合計して total_calories に格納


    return render(request, 'diet/list.html', {'meals': meals, 'total_calories': total_calories})
    #meals と total_calories をテンプレート meal_list.html に渡す。
    #食事リスト（meals）と合計カロリー（total_calories）を表示するためにこれらの値を使用する。
    #total_calories は、meals のカロリーの合計


def add_meal(request):
    if request.method == 'POST'  #フォームが送信されたときに処理を開始する

    
        form = MealForm(request.POST)  #MealForm は、食事データを入力するためのクラスで,このクラスは、食事の名前やカロリーなどを取得するためのフィールド
        
        if form.is_valid():   #form.is_valid() は、フォームのデータが正しいかチェックする
            form.save()  # 食事データを保存
            return redirect('meal_list')  #保存されたデータをmeal_listに返す
    else:
        form = MealForm() #フォームがまだ送信されていない場合や、送信されたデータが無効だった場合に、新しいフォームを表示する

    return render(request, 'meals/add_meal.html', {'form': form}) #フォームの初期表示や、入力ミスがあった場合に再表示するための準備