from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

recipes = [
    {
        'id': 1,
        'name': 'Spaghetti Carbonara',
        'ingredients': [
            '200g spaghetti',
            '100g pancetta',
            '2 large eggs',
            '50g pecorino cheese',
            '50g parmesan',
            'Freshly ground black pepper',
            'Salt',
            '1 clove of garlic, peeled',
            '50g unsalted butter',
        ],
        'instructions': [
            'Put a large saucepan of water on to boil.',
            'Finely chop the pancetta, having first removed any rind.',
            'Finely grate both cheeses and mix them together.',
            'Beat the eggs in a medium bowl, season with a little freshly grated black pepper and set everything aside.',
            'Add 1 tsp salt to the boiling water, add the spaghetti and when the water comes back to the boil, cook at a constant simmer.',
            'Squash the garlic with the blade of a knife, just to bruise it.',
            'Melt the butter in a large frying pan, add the pancetta and garlic, and cook for about 5 minutes until the pancetta is golden and crisp.',
            'Remove and discard the garlic.',
            'Keep the heat under the pancetta on low. When the pasta is ready, lift it from the water with a pasta fork or tongs and put it in the frying pan with the pancetta. Don’t throw away the pasta water.',
            'Mix most of the cheese in with the eggs, keeping a small handful back for sprinkling over later.',
            'Take the pan of spaghetti and pancetta off the heat.',
            'Quickly pour in the eggs and cheese. Using tongs or a long fork, lift up the spaghetti so it mixes easily with the egg mixture.',
            'Add extra pasta cooking water to keep it saucy. You don’t want scrambled eggs, but a creamy texture.',
            'Serve immediately with a little sprinkling of the remaining cheese and a grating of black pepper.',
        ],
        'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS6FTv-lJYSJ5f24cs_y72ttvTBS2vBOZ5rkw&s',
        'description': 'A classic Italian pasta dish.'
    },
    {
        'id': 2,
        'name': 'Chicken Alfredo',
        'ingredients': [
            '200g fettuccine',
            '2 chicken breasts',
            '2 cups heavy cream',
            '1/2 cup grated parmesan cheese',
            '2 cloves garlic, minced',
            'Salt and pepper to taste',
            '2 tablespoons olive oil',
            'Parsley for garnish',
        ],
        'instructions': [
            'Cook the fettuccine according to package instructions.',
            'In a large pan, heat olive oil over medium heat.',
            'Season the chicken breasts with salt and pepper, and cook in the pan until golden and cooked through.',
            'Remove the chicken from the pan and set aside.',
            'In the same pan, add minced garlic and cook for 1 minute.',
            'Add heavy cream and bring to a simmer.',
            'Stir in grated parmesan cheese until the sauce thickens.',
            'Slice the cooked chicken and add to the sauce.',
            'Toss the cooked fettuccine in the sauce.',
            'Garnish with parsley and serve immediately.',
        ],
        'image': 'https://eatinginaninstant.com/wp-content/uploads/2022/08/IP-Chicken-Alfredo-8-1200-500x500.jpg',
        'description': 'A creamy pasta dish with chicken.'
    },
]

@api_view(['GET'])
def recipe_list(request):
    return Response(recipes)

contact = [
   {
        'name': 'Shruthi Vallap Reddy',
        'phone': '+1(913)-749-8998',
        'address': [ 
        '31235 Hastings Creek Lane',
         'Fulshear , Texas',
         '77441-2449',
         'United States'
        ]
   }
]
@api_view(['GET'])
def contact_list(request):
    return Response(contact)

