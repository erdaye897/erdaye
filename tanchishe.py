while True :
    #变量初始化
    KEY = 'up'
    lKEY = KEY
    x, y = 240, 240
    path = []
    path.append((x, y))
    fx, fy = random.randrange(20, 460, 20), random.randrange(20, 460, 20)
    while path.count((fx, fy)) != 0 :
        fx, fy = random.randrange(20, 460, 20), random.randrange(20, 460, 20)
    T = 0
    M = 0
    B = True
 
    while True :
        time.sleep(0.1)
 
        #检测是否按下退出按钮
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                exit()
        
        #检测键盘按键
        if (KEY == 'up' and lKEY != 'down') or (KEY == 'w' and lKEY != 's') :
            y -= 20
            lKEY = KEY
        elif (KEY == 'down' and lKEY != 'up') or (KEY == 's' and lKEY != 'w')  :
            y += 20
            lKEY = KEY
        elif (KEY == 'left' and lKEY != 'right') or (KEY == 'a' and lKEY != 'd')  :
            x -= 20
            lKEY = KEY
        elif (KEY == 'right' and lKEY != 'left') or (KEY == 'd' and lKEY != 'a')  :
            x += 20
            lKEY = KEY
        elif KEY == 'alt' or KEY == 'right alt' :
            B = False
            while True :
                pygame.event.wait()
                if KEY == 'space' :
                    KEY = lKEY
                    B = True
                    break
                elif KEY == 'esc' :
                    pygame.quit()
                    if M > HI :
                        HI = M
                        db.set('HiMark', HI)
                        db.dump()
                    exit()
            continue
        elif KEY == 'esc' :
            pygame.quit()
            if M > HI :
                HI = M
                db.set('HiMark', HI)
                db.dump()
            exit()
        else :
            KEY = lKEY
            continue
 
        #检测是否碰撞或吃掉食物
        if crash() :
            break
        if eat() :
            M += 1
            fx, fy = random.randrange(20, 460, 20), random.randrange(20, 460, 20)
            while path.count((fx, fy)) != 0 :
                fx, fy = random.randrange(20, 460, 20), random.randrange(20, 460, 20)
        else :
            del path[0]
        
        #更新屏幕内容
        path.append((x, y))
        screen.fill('black')
        snake()
        food()
        timer()
        mark()
        hi()
        pygame.display.flip()
 
    #保存最高纪录
    if M > HI :
        HI = M
        db.set('HiMark', HI)
        db.dump()
    
    B = False
 
    #检测是否退出或再来一局
    while True :
        event = pygame.event.wait()
        if event.type == pygame.QUIT :
            pygame.quit()
            exit()
        elif KEY == 'esc' :
            pygame.quit()
            exit()
        elif KEY == 'return' or KEY == 'enter' :
            break
