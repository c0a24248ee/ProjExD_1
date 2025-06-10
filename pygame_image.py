import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg") #背景画像のsurface
    bg_img2 = pg.transform.flip(bg_img, True, False)
    kk_img = pg.image.load("fig/3.png") #こうかとんの画像のsurface
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300, 200

    tmr = 0
    move =[0, 0]
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_list = pg.key.get_pressed() #キーの押下状態を取得
        if key_list[pg.K_UP]:
            move = [-1, -1] #上キーが押されたら上に移動
        elif key_list[pg.K_DOWN]:
            move = [-1, 1]
        elif key_list[pg.K_LEFT]:
            move = [-1, 0]
        elif key_list[pg.K_RIGHT]:
            move = [1, 0]
        else:
            move = [-1, 0]
        kk_rct.move_ip(move)
        x = tmr%3200

        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img2, [-x+1600, 0])
        screen.blit(bg_img, [-x+3200, 0])
        #screen.blit(kk_img, [300, 200])
        screen.blit(kk_img, kk_rct)
        pg.display.update()
        tmr += 1      
        #print(tmr, x)  
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()