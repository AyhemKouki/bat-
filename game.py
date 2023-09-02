import pygame , sys , random

def start_menu():
    pygame.init()
    width,height = 400 , 587
    screen = pygame.display.set_mode((width,height))
    menu = pygame.image.load('C:/Users/hp/Desktop/bat/assests/start menu.png')
    menu_rect = menu.get_rect(center =(width/2 , height/2))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main_game()
        screen.blit(menu, menu_rect)
        pygame.display.update()

def game_over (score):
    pygame.init()
    width,height = 400 , 587
    screen = pygame.display.set_mode((width,height))
    game_ver = pygame.image.load('C:/Users/hp/Desktop/bat/assests/game over.png')
    game_over_rect = game_ver.get_rect(center =(width/2 , height/2))
    game_font = pygame.font.Font(None,80)
    score_x =200
    score_y = 100
    score_text = 'score : '+str(score)
    score_surface = game_font.render(score_text,True,(255,255,255))
    score_rect=  score_surface.get_rect(center=(score_x,score_y))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    main_game()
        screen.blit(game_ver, game_over_rect)
        screen.blit(score_surface,score_rect)
        pygame.display.update()

        
def main_game():
    def create_spike():
        x = random.randint(15,385)
        new_spike = spike_image.get_rect(center = (x , -15))
        return new_spike
    def draw_spike(spikes):
        for spike in spikes:
            screen.blit(spike_image, spike)
    def move_spikes(spikes):
        for spike in spikes:
            spike.centery += 5
        return spikes
    def collision_with_spike(spikes):
        for spike in spikes:
            if spike.collidepoint(bat_rect.centerx,bat_rect.centery):
                game_over(score)
    def create_coin():
        test = True
        while(test):
            x = random.randint(15,390)
            y = random.randint(15,500)
            if (x % 15 == 0):
                new_coin_rect = coin_image.get_rect(center = (x,y))
                test = False
        return new_coin_rect
    def calculate_score(score): 
        score_x =350
        score_y = 550
        score_text = 'score : '+str(score)
        score_surface = game_font.render(score_text,True,(255,255,255))
        score_rect=  score_surface.get_rect(center=(score_x,score_y))
        screen.blit(score_surface,score_rect)
    pygame.init()

    spike_list = []
    width,height = 400 , 587
    score = 0

    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption('bat game')

    bg_image = pygame.image.load('C:/Users/hp/Desktop/bat/assests/bg.png').convert_alpha()

    bat_image = pygame.image.load('C:/Users/hp/Desktop/bat/assests/bat-up.png').convert_alpha()
    bat_rect = bat_image.get_rect(center =(width/2 , 400))

    spike_image = pygame.image.load('C:/Users/hp/Desktop/bat/assests/spike.png').convert_alpha()
    spike_image = pygame.transform.flip(spike_image,False,True)

    coin_image = pygame.image.load('C:/Users/hp/Desktop/bat/assests/coin.png').convert_alpha()
    coin_rect = create_coin()

    game_font = pygame.font.Font(None,25) 

    sound_effect = pygame.mixer.Sound('C:/Users/hp/Desktop/bat/sound/coin sound.mp3')
    sound_effect.set_volume(0.2 )

    clock = pygame.time.Clock()

    SPAWNSPIKE = pygame.USEREVENT
    pygame.time.set_timer(SPAWNSPIKE , 1000)

    gravity = 0.2
    jump_height = 5
    y_velocity = jump_height
    jump = False
    bat_move = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type  == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE :
                    jump = True
                    bat_move = 0
                if event.key == pygame.K_LEFT :
                    bat_rect.centerx -= 30
                if event.key == pygame.K_RIGHT :
                    bat_rect.centerx += 30
            if event.type == SPAWNSPIKE :
                spike_list.append(create_spike())
        if jump:
            bat_rect.centery -= y_velocity
            y_velocity -= gravity
            if y_velocity < 0:
                jump = False
                y_velocity = jump_height
        else:
            bat_move += gravity
            bat_rect.centery += bat_move
        if coin_rect.collidepoint(bat_rect.centerx,bat_rect.centery):
            sound_effect.play()
            coin_rect = create_coin()
            score += 1
            
        screen.blit(bg_image,(0,0))
        screen.blit(coin_image,coin_rect)
        screen.blit(bat_image,bat_rect)
        calculate_score(score)
        draw_spike(spike_list)
        spike_list  = move_spikes(spike_list)
        collision_with_spike(spike_list)
        clock.tick(60)
        pygame.display.update()


start_menu()