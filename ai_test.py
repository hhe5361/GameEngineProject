import pygame
from pygame.locals import QUIT, K_UP, K_DOWN, K_LEFT, K_RIGHT, K_SPACE
from Object.GameObject import Transform, GameObject
from Ai.ai_engine import SimpleAI
import random  # 랜덤 모듈 추가

# Pygame 초기화
pygame.init()

# 게임 창 설정
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple AI Simulation")
clock = pygame.time.Clock()

# 플레이어 오브젝트 생성
player_transform = Transform(x=WIDTH // 2, y=HEIGHT // 2)
player = GameObject(transform=player_transform, name="Player")

# AI 오브젝트들을 랜덤한 위치에 생성
ai_positions = [(random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)) for _ in range(10)]

ai_objects = []
for i, ai_position in enumerate(ai_positions):
    ai_transform = Transform(x=ai_position[0], y=ai_position[1])
    ai = SimpleAI(transform=ai_transform, player=player, name=f"AI{i}")
    ai_objects.append(ai)
    
game_started = False

# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()

        # 스페이스바를 눌렀을 때 게임 시작
        if event.type == pygame.KEYDOWN and event.key == K_SPACE:
            game_started = True

    # 게임이 시작되지 않았다면 아무 동작도 하지 않음
    if not game_started:
        continue

    # 플레이어 이동
    keys = pygame.key.get_pressed()
    player.transform.x += (keys[K_RIGHT] - keys[K_LEFT]) * 5
    player.transform.y += (keys[K_DOWN] - keys[K_UP]) * 5

    # Delta time 계산
    delta_time = clock.tick(FPS) / 1000.0  # 밀리초를 초로 변환

    # AI 업데이트 및 렌더링
    screen.fill((0, 0, 0))
    player.render(screen, (255, 0, 0))
    for ai in ai_objects:
        ai.implement_simple_ai(delta_time)
        ai.render(screen, (0, 0, 255))

    pygame.display.flip()
    clock.tick(FPS)
