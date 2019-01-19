class Settings():
    """A class to store all settings"""

    def __init__(self):
        """Initialize game static settings"""

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 10

        # Level up acceleration
        self.speedup_scale = 1.1

        # Alien point increase after levels
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ Initialize dynamic settings """
        self.ship_speed_factor = 10
        self.bullet_speed_factor = 25
        self.alien_speed_factor = 1

        # fleet direction
        self.fleet_direction = 1

        # scoring
        self.alien_points = 5

    def increase_speed(self):
        """Increase speed settings and alien point values"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)