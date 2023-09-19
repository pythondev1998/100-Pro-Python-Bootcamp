class CollisionHandler:
    @staticmethod
    def check_collision(ball, obj):
        if ball.distance(obj) < 20:
            return True
        return False

# Comentario:
# La clase CollisionHandler proporciona métodos estáticos para comprobar colisiones
# entre la bola y otros objetos del juego, como la pala o los ladrillos.
