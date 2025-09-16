from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass', team=self.team)
        self.activity = Activity.objects.create(user=self.user, type='run', duration=30, calories=300)
        self.workout = Workout.objects.create(name='Test Workout', description='desc', duration=20)
        self.leaderboard = Leaderboard.objects.create(team=self.team, points=100)

    def test_user_team(self):
        self.assertEqual(self.user.team, self.team)

    def test_activity_user(self):
        self.assertEqual(self.activity.user, self.user)

    def test_leaderboard_team(self):
        self.assertEqual(self.leaderboard.team, self.team)

    def test_workout_name(self):
        self.assertEqual(self.workout.name, 'Test Workout')
