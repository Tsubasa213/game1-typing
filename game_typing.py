import pygame
import sys
import random
import time


# Pygameの初期化
pygame.init()

# スコアの初期化
score = 0

easy_words_a = ["anpanman","ringo","neko","hituji","karaoke","tora","saihu","miso","banana","budou","okaki","mikan"]
easy_words_b = ["アンパンマン","りんご","ねこ","ひつじ","カラオケ","とら","さいふ","みそ","バナナ","ぶどう","おかき","みかん"]

normal_words_a = ["ryokousaki","ra-men"]
normal_words_b = ["旅行先","ラーメン"]

hard_word_a = ["dhizuni-rando"]
hard_word_b = ["ディズニーランド"]

# 画面の設定
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('タイピングゲーム')

# 色の定義
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# フォントの設定
font = pygame.font.Font(None, 50)

font_path = "C:/Windows/Fonts/meiryo.ttc" 
# 日本語対応のフォントをロード
japanese_font = pygame.font.Font(font_path, 36)

# タイピングゲームの状態
timer = 100  # タイマーの初期値（秒）
start_ticks = pygame.time.get_ticks()  # タイマー開始時間
consecutive_correct = 0  # 連続正解数
mistakes = 0  # 誤答数
current_word = ''
user_input = ''
word_index = 0

# 難易度のリスト
difficulties = ['Easy', 'Normal', 'Hard']
current_selection = 0

# 難易度を描画する関数
def draw_menu():
    screen.fill(BLACK)
    for i, difficulty in enumerate(difficulties):
        label = japanese_font.render(difficulty, True, BLUE if i == current_selection else WHITE)
        position = label.get_rect(center=(screen_width // 2, screen_height // 2 + i * 60))
        screen.blit(label, position)

# タイピングゲームを開始する関数
def start_typing_game(difficulty):
    global current_word, user_input, word_index, timer, start_ticks, consecutive_correct, mistakes, score, current_selection
    global word_list, display_list
    if difficulty == 'Easy':
        word_list = easy_words_a
        display_list = easy_words_b
    elif difficulty == 'Normal':
        word_list = normal_words_a
        display_list = normal_words_b
    elif difficulty == 'Hard':
        word_list = hard_word_a
        display_list = hard_word_b

    word_index = random.randint(0, len(word_list) - 1)
    current_word = word_list[word_index]
    display_word = display_list[word_index]
    display_word_surface = japanese_font.render(display_word, True, WHITE)
    user_input_surface = japanese_font.render(user_input, True, WHITE)

    # タイマーの初期化
    timer = 10  # タイマーの初期値（秒）
    start_ticks = pygame.time.get_ticks()  # タイマー開始時間
    consecutive_correct = 0  # 連続正解数
    mistakes = 0  # 誤答数
    

    # タイピングゲームループ
    typing_game_running = True
    while typing_game_running:
        # タイマーの更新
        current_ticks = pygame.time.get_ticks()
        seconds_passed = (current_ticks - start_ticks) / 1000.0
        timer -= seconds_passed
        start_ticks = current_ticks

            
        
        # イベント処理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                elif event.key == pygame.K_RETURN:
                    if user_input == current_word:
                        score += 1000
                        consecutive_correct += 1
                    else:
                        score -= 500
                        mistakes += 1
                    # 新しい単語を選ぶ
                    word_index = random.randint(0, len(word_list) - 1)
                    current_word = word_list[word_index]
                    display_word = display_list[word_index]
                    user_input = ''
                else:
                    user_input += event.unicode

        # 画面の描画
        screen.fill(BLACK)
        display_word_surface = japanese_font.render(display_word, True, WHITE)  # 日本語フォントを使用
        user_input_surface = japanese_font.render(user_input, True, WHITE)  # 日本語フォントを使用
        screen.blit(display_word_surface, (50, 100))
        screen.blit(user_input_surface, (50, 200))
        # タイマーの描画（画面の右上に表示）
        timer_surface = japanese_font.render(f"{timer:.2f}", True, WHITE)
        timer_rect = timer_surface.get_rect(topright=(screen_width - 10, 10))
        screen.blit(timer_surface, timer_rect)
        # スコアの描画（画面の右下に表示）
        score_surface = japanese_font.render(f"スコア: {score}", True, WHITE)
        score_rect = score_surface.get_rect(bottomright=(screen_width - 10, screen_height - 10))
        screen.blit(score_surface, score_rect)

        # タイマーが0になったらスコア画面を表示
        if timer <= 0:
            typing_game_running = False
            # 半透明の背景
            overlay = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 128))  # 半透明の黒
            screen.blit(overlay, (0, 0))
            # スコアと正解数、間違った数のテキスト
            score_text = f"スコア: {score}"
            correct_text = f"正解数: {consecutive_correct}"
            mistakes_text = f"間違った数: {mistakes}"
            texts = [score_text, correct_text, mistakes_text]
            # テキストを画面の真ん中に上から順に表示
            for i, text in enumerate(texts):
                text_surface = japanese_font.render(text, True, WHITE)
                text_rect = text_surface.get_rect(center=(screen_width // 2, screen_height // 2 - 50 + i * 50))
                screen.blit(text_surface, text_rect)
            pygame.display.flip()
            # エンターキーが押されるまで待機
            waiting_for_enter = True
            while waiting_for_enter:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            waiting_for_enter = False
                            # スコアと打った文字をリセット
                            score = 0
                            consecutive_correct = 0
                            mistakes = 0
                            user_input = ''

        # スコアが0以下の場合はマイナスを表示
        score_text = f"スコア: {score}" if score >= 0 else f"スコア: -{abs(score)}"
        score_surface = japanese_font.render(score_text, True, WHITE)
        score_rect = score_surface.get_rect(bottomright=(screen_width - 10, screen_height - 10))
        screen.blit(score_surface, score_rect)

        # 画面の更新
        pygame.display.flip()

# メインループ
running = True
while running:
    draw_menu()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                current_selection = (current_selection - 1) % len(difficulties)
            elif event.key == pygame.K_DOWN:
                current_selection = (current_selection + 1) % len(difficulties)
            elif event.key == pygame.K_RETURN:
                selected_difficulty = difficulties[current_selection]
                start_typing_game(selected_difficulty)
    pygame.display.flip()




# Pygameの終了
pygame.quit()
sys.exit()


# 今後すること

# スコア機能の実装
# 注意点
# 一つ正解するたびに何点追加するのかを決める
# どこにスコアを表示するのかを決める(例えばタイマーの下とか)

# フィニッシュ画面の追加
# ゲームが終わったときフィニッシュ画面に行くようにする
# 注意点
# 字は何を表示するか(フィニッシュの文字とスコアだけでいいのか)
# どこに何色で表示するのか
# 背景は半透明なのか何か色を設定するのか


# 時間があれば…

# ゲームを実行中にプレイヤーが入力しているとき，今入力している文字だけ色が変わるようにする
# →そのためにはあらかじめ灰色などでローマ字を表示して現在入力しているところのみ赤色にするなどのプログラムが必要

# リトライできる機能を作る
# →そのためにはフィニッシュ画面で何らかの動作をするともう一度ゲームが実行されて何らかの動作をすると終了するようにするプログラムを作る
# たとえばエンターキーを押すともう一度できて，エスクキーで終了など
# またリトライしたら過去のベストスコアを参照(表示)出来るようにしているとなおゲーム性が出てくる

# 一つの単語を入力できる時間にも制限をつける
# →寿司打も寿司が流れている間に文字を打つ必要がある．だからそれと同じくゲーム全体だけでなく各単語ごとにもタイマーを実装する必要がある．