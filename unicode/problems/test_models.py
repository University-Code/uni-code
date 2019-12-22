from django.test import TestCase
from problems.models import Problem, Upvote, DATATYPE_CHOICES
from users.models import User


def create_user(username, password):
    """
    Create a user for dummy testing data.
    """
    return User.objects.create(username=username, password=password)

def create_problem(creator, title, description, datatype, example_solution):
    """
    Create a problem with the given arguments.
    """
    
    return Problem.objects.create(creator=creator,
                                  title=title,
                                  description=description,
                                  datatype=datatype,
                                  example_solution=example_solution)

class ProblemModelTests(TestCase):

    def test_to_dict_values(self):
        user = create_user('jp', 'password')
        problem = create_problem(creator=user,
                                 title='Testing Dict Title',
                                 description='this is a test decription',
                                 datatype="String",
                                 example_solution='This is a dict example solution')
        d = problem.to_dict(user=create_user('testuser', 'password'))
        self.assertIs(d['id'], problem.id)
        self.assertIs(d['title'], problem.title)
        self.assertIs(d['creator'], problem.creator)
        self.assertIs(d['upvotes'], 0)
        self.assertIs(d['upvoted'], False)

    def test_set_upvoted_true(self):
        user = create_user('jp', 'password')
        problem = create_problem(creator=user,
                                 title='Testing Dict Title',
                                 description='this is a test decription',
                                 datatype="String",
                                 example_solution='This is a dict example solution')
        problem.set_upvoted(user=user, upvoted=True)
        upvoted_problem = Upvote.objects.filter(id=user.id)
        self.assertIs(upvoted_problem.count(), 1)
        self.assertEquals(upvoted_problem[0].user, user)
        self.assertEquals(upvoted_problem[0].problem, problem)

    def test_set_upvoted_false(self):
        user = create_user('jp', 'password')
        problem = create_problem(creator=user,
                                 title='Testing Dict Title',
                                 description='this is a test decription',
                                 datatype="String",
                                 example_solution='This is a dict example solution')
        problem.set_upvoted(user=user, upvoted=True)
        upvoted_problem = Upvote.objects.filter(id=user.id)
        problem.set_upvoted(user=user, upvoted=False)
        self.assertIs(upvoted_problem.count(), 0)
        

        
