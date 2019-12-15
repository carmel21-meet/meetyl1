users = []
posts = []
comment_list = []
class User():
	def __init__(self,name,email,password):

	 	self.name=name
	 	self.email=email
	 	self.password=password
	 	self.friend_list=[]
	 	self.posts=[]

	def add_friend(self,email):
	 	self.friend_list.append(email)
	 	print(self.name + " has added " + email + " as a friend")

	def remove_friend(self,email):
	 	self.friend_list.remove(self.email)
	 	print(self.name + "has remove" + email + "as a friend")

	def post(self,text):
	 	self.text=text
	 	self.posts.append(text)
	 	print(self.name + "has posted" + text)

	def get_userInfo(self):
	 	print("Name: " + self.name)
	 	print("Email: " + self.email)
	 	print("password: " + self.password)
	 	print(self.friend_list)
	 	print(self.posts)

user1 = User("Ananas","Ananas@gmail.com","12345")
user2 = User("Diam","Diam@gmail.com","12345")
user1.add_friend("Ananas@gmail.com")
user1.post(" idk")
user1.get_userInfo()
user1.remove_friend("Diam@gmail.com")

class Post():
	def __init__(self,text,picture):
		text = self.text
		picture = self.picture

	def add_post(self,text,picture):
		self.posts_list.append(text,picture)
		print(self.name + " has posted " + text + " and has posted " + picture)
class Comment(Post):
	def __init__(self,name):
		self.name = name
	def comment(self,text):
		comment_list.append(text)
		print(self.name + " has commented " , text)
comment1 = Comment("Mousa")
comment1.comment("Heello")


