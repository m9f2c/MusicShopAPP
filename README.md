# MusicShopAPP
Music Shop with Django

Heroku web: https://fierce-reaches-98501.herokuapp.com/

Login Admin:
* username: admin
* password: qwer1234

Login User1:
* username: user1
* password: qwer1234

Login User2:
* username: user2
* password: qwer1234

Hem afegit un model de dades (User_Recording_Sell) dins de PersonalPage, en el qual guardem els Recordings afegits per cadascun dels usuaris de la nostra aplicació. Aquest nou model està relacionat amb l'entitat Artist i amb Recording, ja que guardem un Recording mitjançant l'artista al qual pertany, títol del Recording, una descripció del recording a vendre, preu de venda i l'usuari que el vol vendre.

Quan afegeixes un nou 'recording' per vendre, es crea les instancies de 'artist' i 'recording' en cas de que no existeixin. Si ja existeixen, no sen creen dues i s'utilitza la que ja esta creada.

Els usuaris poden editar i eliminar els seus 'recordings'.





