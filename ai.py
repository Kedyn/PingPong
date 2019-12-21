class AI:
    """Simple AI control."""

    def __init__(self, paddles, ball):
        self.paddles = paddles
        self.ball = ball

    def set_difficulty(self, difficulty):
        speed = self.paddles[0].speed_factor

        if difficulty is "easy":
            speed *= 0.4
        elif difficulty is "average":
            speed *= 0.6

        for i in range(len(self.paddles)):
            self.paddles[i].speed_factor = speed

    def update(self):
        for i in range(len(self.paddles)):
            self.paddles[i].moving_positive = False
            self.paddles[i].moving_negative = False
            if self.paddles[i].side is 1 or self.paddles[i].side is 5:
                if self.paddles[i].rect.centery < self.ball.rect.centery:
                    self.paddles[i].moving_positive = True
                elif self.paddles[i].rect.centery > self.ball.rect.centery:
                    self.paddles[i].moving_negative = True
            else:
                if self.paddles[i].rect.centerx < self.ball.rect.centerx:
                    self.paddles[i].moving_positive = True
                elif self.paddles[i].rect.centerx > self.ball.rect.centerx:
                    self.paddles[i].moving_negative = True
