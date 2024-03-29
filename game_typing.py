import pygame
import sys
import random


# Pygameの初期化
pygame.init()

# スコアの初期化
score = 0

easy_words_a = ["anpanman","ringo","neko","hituji","karaoke","tora","saihu","miso","banana","budou","okaki","mikan","hontou","tenki","taberu","gakkou","hanabi","benkyou","undou","utau","kuuki","tanosii","eiga","hasiru","ongaku","tisiki","jikan","hayai","sensei","akarui","situmon","oisii","hanasu","aoi","egao","yoi","imi","midori","ame","syasin","ryokou","kiru","kaku","syousetu","kanasii","doubutu","iro","heya","siru","omou","yasumu","kau","denwa","asa","mati","okane","kuruma","kusa","hikari","tori","siranai","atatakai","tegami","yoru","miti","genki","e","wasureru","basyo","okiru","huku","asobu","warui","yorokobu","ie","tyousyoku","isogu","kutu","noru","oto","kiru","inu","yuki","kao","okoru","tuyoi","hurui","nimotu","amai","nemuru","owaru","marui","hajimaru","naru","atui","sigoto","takai","tooi","kantan","oyogu","hajimete","kaeru","nozomu","nomu","sizuka","kowai","gakki","hiraku","tomaru","te","isogasii","hiroi"]
easy_words_b = ["アンパンマン","りんご","ねこ","ひつじ","カラオケ","とら","さいふ","みそ","バナナ","ぶどう","おかき","みかん","本当","天気","食べる","学校","花火","勉強","運動","歌う","空気","楽しい","映画","走る","音楽","知識","時間","速い","先生","明るい","質問","美味しい","話す","青い","笑顔","良い","意味","緑","雨","写真","旅行","着る","書く","小説","悲しい","動物","色","部屋","知る","思う","休む","買う","電話","朝","町","お金","車","草","光","鳥","知らない","暖かい","手紙","夜","道","元気","絵","忘れる","場所","起きる","服","遊ぶ","悪い","喜ぶ","家","朝食","急ぐ","靴","乗る","音","切る","犬","雪","顔","起こる","強い","古い","荷物","甘い","眠る","終わる","丸い","始まる","鳴る","暑い","仕事","高い","遠い","簡単","泳ぐ","初めて","帰る","望む","飲む","静か","怖い","楽器","開く","止まる","手","忙しい","広い"]

normal_words_a = ["ryokousaki","ra-men","hanranbunsi","jikkenjissyuu","kateika","pettosyoppu","komyunithi","kenkousindan","o-rudofassyon","toukyoutawa-","syanhai","kyoukankaku","jindousyugi","tyuusyouka","kagakutekisyuhou","biseibutugaku","kasika","kobetuka","titekizaisan","jizokukanousei","seimitukiki","syakaitekieikyou","paradaimusihuto","titekisouzou","utyuuron","sinkasinrigaku","idensiryouhou","inobe-syon","souzouseisikou","guro-baruka","ri-da-sippu","hukuzatusei","ryousirikigaku","tisikikeizai","seisinbunseki","baioesikkusu","koujigen","rezonensu","tyouetusei","singyurarithi","pa-sonarithi","kuusoukagaku","purototaipingu","episutemoroji-","paradokkusu","morarithi"]
normal_words_b = ["旅行先","ラーメン","反乱分子","実験実習","家庭科","ペットショップ","コミュニティ","健康診断","オールドファッション","東京タワー","上海","共感覚","人道主義","抽象化","科学的手法","微生物学","可視化","個別化","知的財産","持続可能性","精密機器","社会的影響","パラダイムシフト","知識創造","宇宙論","進化心理学","遺伝子療法","イノベーション","創造性思考","グローバル化","リーダーシップ","複雑性","量子力学","知識経済","精神分析","バイオエシックス","高次元","レゾネンス","超越性","シンギュラリティ","パーソナリティ","空想科学","プロトタイピング","エピステモロジー","パラドックス","モラリティ"]

hard_word_a = ["dhizuni-rando","osyakasama","maindokontoro-ru","toukyoutokkyokyokakyoku","komyunike-shonnouryoku","chouetutekikeiken","konpyu-tabijon","interijentoe-jento","guro-barunabige-shon","haipa-pafo-mansu","rejirientonettowa-ku","marutimo-daruinta-fe-su","inobe-shonekoshisutemu","enbaiomentarizumu","guro-barumegatorendo","konpyu-te-shonarudezain","inhurasutorakuchamanejimento","maruchisuke-ruapuro-ti","dejitarutuintekunoroji-","shingyurarithiibento","de-tafyu-jontekunoroji-","ba-charuriarithiekusuperiensu","intarakuthibua-tofi-rudo","burrokutye-ntekunoroji-","nonbaiorojikaruraihu","saiba-sekyurithipurotokoru","interijentorimo-tosensingu","bbigude-taanarithikusu","sasutenabirithiinobe-shon"]
hard_word_b = ["ディズニーランド","お釈迦様","マインドコントロール","東京特許許可局","コミュニケーション能力","超越的経験","コンピュータビジョン","インテリジェントエージェント","グローバルナビゲーション","ハイパーパフォーマンス","レジリエントネットワーク","マルチモーダルインターフェース","イノベーションエコシステム","エンバイオメンタリズム","グローバルメガトレンド","コンピューテーショナルデザイン","インフラストラクチャマネジメント","マルチスケールアプローチ","デジタルツインテクノロジー","シンギュラリティイベント","データフュージョンテクノロジー","バーチャルリアリティエクスペリエンス","インタラクティブアートフィールド","ブロックチェーンテクノロジー","ノンバイオロジカルライフ","サイバーセキュリティプロトコル","インテリジェントリモートセンシング","ビッグデータアナリティクス","サステナビリティイノベーション"]

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
    timer = 60  # タイマーの初期値（秒）
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

#レイアウトを整える
#単語増やす
#注意書きの実装