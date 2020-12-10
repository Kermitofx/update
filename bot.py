import telebot
import os, sys
from random import randint, choice
import model
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, \
    ReplyKeyboardRemove

token = "1356643015:AAFs6glUlosstXAoMQkmOTSyuQ8mkerrl78"
bot = telebot.TeleBot(token)

post_dict = {}  # saves posts data while user's working on it
storage_channel_id = "@DextyOficial"  # channel's id to send final results to

def gen_markup():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('❤| Canal Official',
                                          url='https://telegram.me/Fakesofc'))
    markup.add(types.InlineKeyboardButton('▶| Sad Station',
                                          url='https://telegram.me/Sad_Station'))

    return markup

def main_menu_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("Criar postagem", callback_data="create_post"))
    
    return markup


def post_markup(message):
    post = post_dict[message.chat.id]
    word = post.words[-1]
    definition_number = len(word.definitions) + 1
    markup = InlineKeyboardMarkup() 
    add_definition_button = InlineKeyboardButton("Adicionar definição#{0}".format(definition_number),callback_data="add_definition")
    add_tags_button = InlineKeyboardButton("Adicionar tags", callback_data="add_tags")
    add_links_button = InlineKeyboardButton("Adicionar links de dicionário", callback_data="add_links")
    add_synonyms_button = InlineKeyboardButton("Adicionar sinônimos", callback_data="add_synonyms")
    add_new_word_button = InlineKeyboardButton("Adicionar nova palavra", callback_data="add_new_word")
    cancel_button = InlineKeyboardButton("❎Cancelar", callback_data="cancel")
    finish_button = InlineKeyboardButton("☑️Pronto", callback_data="finish")

    markup.add(cancel_button, finish_button)

    return markup


def skip_markup():
    markup = ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(KeyboardButton('[OK]'))
    return markup


##def parts_of_speech_markup():
######    markup = ReplyKeyboardMarkup(one_time_keyboard=True)
######    markup.add(KeyboardButton('📝 Dexty Official '))
###    return markup


def send_to_storage_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("[ ☑️ ] Enviar", callback_data="send_to_storage"),
               InlineKeyboardButton("[ 📝 ] Editar", callback_data="edit_before_sending"),
               InlineKeyboardButton("[ ❎ ] Cancelar", callback_data="cancel_sending_to_storage"),)
    return markup


@bot.message_handler(commands=['start'])
def process_start(message):
    bot.send_message(message.chat.id, "📝Crie uma nova postagem aqui.",
                     reply_markup=main_menu_markup())

@bot.message_handler(commands=["indireta"])
def frase_command(m):
	if m.text == '/indireta' or m.text == '/indireta@DextyRobot':
		list = ["Não entre na infantil disputa de quem se importa menos. ","O tempo não muda pessoas, só mostra quem elas realmente são. ", "Oportunidade se espera andando! ","Por pior que seja te deixar pra trás, não nasci pra morrer esperando alguém que nunca vai ficar","Ou entre na minha linha ou saia da minha reta. ", "Larga mão de quem não tá afim de segurar a sua ", "Se tudo for abismo, invente asas. ", "Não olhe pra trás. Não tem nada lá esperando por você. ", "Sorria sem câmera , converse sem celular, ajude sem platéia, ame sem condições ", "Aquela pegada na bunda que chega a te levantar pra cima. ", " Pegada não é só pegar na bunda ", "Se eu te convidar pra fugir será que você aceita? ", "Só o impossível me interessa ", "Eu sou tão foda, que me fodo com a minha fodalidade. ", "É tão estranho ver alguém te chamando de amor, depois que você parou de acreditar no amor.", "Ela sabe aproveitar a vida sem precisar de ninguém.","Não ignore nenhum sorriso, vai que você seja o motivo.", "Pra muitos o céu é o limite. Pra mim o céu é meu lar. ", "A chave para conhecer o amor é não ter fechaduras.", "Eu sei moça, dói sim. Mas a gente cresce, floresce e planta amor em outro alguém "," Não sei, mas eu pensei que desse vez iria dar certo.  "," Todos os dias eu me imagino ao seu lado. "," Te amei no passado, te amo no presente e se o futuro permitir te amarei eternamente. "," O amor é uma aquarela de alegria e uma chuva de emoção. "," Enquanto não acontece, a gente imagina. "," Não destrua seu futuro por problemas do passado. "," Se você não existisse, eu te inventaria. "," Uma lágrima nos ensina a sorrir e um adeus nos ensina a valorizar. "," Éramos inseparáveis, porém sendo sempre separados. "," Você não precisa ir tão longe para encontrar aquilo que mais procura. "," Se choras por ter perdido o sol, as lágrimas o impedirão de ver estrelas. "," Os seus olhos só refletem o que o seu coração está cheio. "," Se você ama duas pessoas ao mesmo tempo, escolha a segunda, porque se você realmente amasse a primeira, nunca teria caído para a segunda. "," A amizade desenvolve a felicidade e reduz o sofrimento, duplicando a nossa alegria e dividindo a nossa dor. "," Quando o amor ou amizade é verdadeiro dura para sempre, não importa a distância, crises e brigas o que as unem é mais forte. "," Não escolha a pessoa mais bonita do mundo, escolha a pessoa que faz do seu mundo o mais bonito. "," No meio dos meus erros, o meu acerto foi você. "," A felicidade é um dom que todos possuímos, mas poucos de nós sabemos utilizá-lo. "," E era você. E tem sido você. E vai continuar sendo você. "," Você tem o seu lado bom e seu lado ruim. Eu escolho os dois para ficar perto de ti. "," Ser diferente não é ser estranho e sim único. "," Não importa a idade ou os momento, existem pessoas que te marcam para vida inteira. "," Por trás de cada doce sorriso, existe uma tristeza amarga que ninguém pode sentir e ver. "," Parabéns pra você que consegue visualizar e não responder, queria ter esse dom. "," Sabe aquele gelo que você me deu? Derreteu, me dê outro aí. "," Não é porque eu estou te tratando bem que estou te dando mole. Se orienta "," Sorria enquanto você ainda tem dentes, porque depois que eu meter a mão na sua cara, vão sumir todos de uma vez. "," Tentar ficar longe de mim não diminui o que eu sinto por você.\n\n— A Culpa é das Estrelas", "Mas no fim do dia, o amor é o que realmente importa.\n\n— The Vampire Diaries", "Botei fé em mim pra viver do meu dom. \n\n— Projota"," Bom, às vezes a vida é dura, mas eu tenho muita coisa para agradecer.\n\n—  A Cabana", "E não se passará um dia, sem que eu sinta a falta do teu sorriso.\n\n— Malévola."," Tudo que vai, volta. O mal que tu faz hoje, amanhã retorna! "," Sim, eu cometi erros. A vida não vem com instruções. "," Primeiro a gente gosta, depois a gente ama, a gente se apega, se fode, e odeia. E depois ainda sente falta. "," Tequila com limão é melhor que sua opinião. "," A esperança mantém segura e firme a nossa vida, assim como âncora mantém seguro o barco. "," A vida é feita de capítulos. Não é porque um foi ruim que você terá que desistir da história inteira. "," Que brotem flores em todos os canteiros de dores."," Uma garota esperta beija mas não ama, ouve mas não acredita, e deixa antes de ser deixada. "," Falsos amigos são como a sombra, só te segue quando o sol está brilhando. "," Se ta contra mim, te desejo boa sorte. "," Se as pessoas fossem chuva, eu era garoa e ela, um furacão. "," Seus olhos tinham o brilho das cores da aquarela, seu cabelo ao vento era a paisagem mais bela. "," Eu vi naquele sorriso tímido todos os sonhos de uma vida inteira. "," Você sabe que uma coisa é certa, estarei lá sempre que você me chamar.\n\n—  Wiz Khalifa."," Bateu uma saudade do teu abraço. "," Eu estou focado na sua boca "," Teu sorriso tem a dose certa pra me fazer feliz. "," Vou te beijar até faltar nosso ar. "," Namore alguem que tire sua roupa e não sua paciência. "," Então sorria, você acordou mais um dia, sorria. "," O plano é bem simples: Ficar com você minha vida inteira. "," Quando alguém duvidar da sua capacidade, não dê atenção, quem tem que saber da sua capacidade é você. "," Só critique se você souber fazer melhor. "," Se o amor acabar é porque nunca foi amor. "," E de mim, será que alguém sente falta?\n\n— Paris, 1925", "Pra que regou as flores se nem se quer ficou pra primavera? "," Meu objetivo era correr do seu lado e não correr atrás de você. "," Nem pense em olhar pra trás, o passado não é seu lugar, você não perdeu nada lá. É pra frente que se anda."," Chique é ser feliz. Elegante é ser honesto. Bonito é ser caridoso. Sábio é ser grato. O resto é inversão de valores. "," Quebrada demais para completar alguém "," Eu não sou flor que se deixe "," Continuo apaixonada, mas agora pela vida "," Infelizmente, esquecer não é o meu forte. "," A gente não combina, a gente se completa. "," Eu tenho medo de você enjoar de mim. "," Tem gente que eu sei que fala mal de mim, mas trato na maior normalidade do mundo. Uns chamam de falsidade, eu chamo de maturidade. "," Há certos momentos na nossa vida que nos mudam para sempre.\n\n— Revenge", "Mensagem boa é aquela que você recebe e sorri assim que vê de quem é. "," Você tem o dom de me fazer ficar bem. "," Queria você aqui, para dormir agarrado comigo. "," Se eu te oferecer todo o meu amor e pizza você fica? "," Não importa a cor do céu, quem faz meu dia mais bonito é você! "," Não há outra mão que eu preferiria segurar, a não ser a sua. "," Eu gosto assim, quando a vida se vinga por mim… "," Relaxa, eu sempre vou te amar, porque no coração a gente não pode mandar. "," Procurando encontrar uma direção nesse mundo de ilusão "," Apaixone-se por Deus em primeiro lugar e ele lhe dará a pessoa certa na hora certa. "," E a vida sorriu quando você chegou. "," E toda vez que chega mensagem eu torço pra ser sua. "," Coração é burro, mas é sincero. "," Orgulho sim. Não nasci para ser segunda opção de ninguém… "," Não abuse da paciência que eu não tenho… "," Meu ciumes é fofo, até começar a voar tijolos. "," Mensagem boa é aquela que te deixa com um sorriso no rosto sem saber o que falar. "," Ai você morre de ciúmes e a pessoa fica falando os detalhes. "," As pessoas se afastam. Aceite isso."," Não sei se é saudade ou costume de pensar em você. "," Alguém me da um coração porque eu já não sinto mais nada. "," Beijo seu rosto, mas queria mesmo era a sua boca. "," Se é para ter fé, não se pode tê-la apenas quando ocorrem milagres.\n\n— Supernatural", "Equilíbrio, tranquilidade e positividade sempre… "," A gente fica triste por cada besteira… "," Era pra ser amizade, mas aí eu me apaixonei. "," Ela é do mundo, ela é da vida, ela é de onde e de quem ela quiser. "," O sol nasce pra todos, a sombra só para alguns… "," A parada é sempre olhar pra frente, manter a cabeça fria, mesmo embaixo do sol quente…"," Deus é a esperança em meio a tempestade. (Jeremias 14:8)"," Ser realista não e apenas dizer verdades, mas também conviver com elas. "," Aquela velha e chata mania de se importa e se foder no fim. "," Eu crio umas paradas na minha mente que nem eu entendo. "," Mas moço, o problema é que uma lágrima puxa a outra "," Ela drink, eu beck, ela pink, eu black. "," Mesmo que você não esteja comigo, eu estou com você.\n\n—  Linkin Park."," Toda história de amor é linda, mas a nossa é a minha favorita. "," Nesse calor eu só queria uma piscina, minha mulher e umas skol beats. "," Você nos meus braços agora, me faria tão bem. ","Eu prometo que tô contigo pro que der e vier… "," Preciso de um café e um cafuné. "," O sorriso dela é diferente de todos os outros. "," Me provoca que eu provoco você em dobro. "," Me leva com você, ou se perde comigo. "," Querido destino: se não é pra mim, não coloque no meu caminho. "," Cadê o tal do “para sempre”, cadê? "," De um modo estranho muito louco parece que em tão pouco tempo meu sentimento é seu.. "," Um homem de verdade se contenta com o que tem, e sabe respeitar a bela mulher que tem. "," Eles se amam em segredo, só esqueceram de contar um para o outro. "," A maldade vai e vem, só o amor permanece. "," Preciso de um bar, de uma conversa boa… Sei lá, me apegar a outras pessoas. "," Como sempre penso: ninguém perde por dar amor, perde quem não sabe receber! "," Então fica mais… fica mais um pouco, porque muito de você pra mim ainda é pouco… "," Já parou pra pensar no que perdeu por não tentar. "," A decepção anula todos os sentimentos bons."," Que tudo seja leve de tal forma que o tempo nunca leva. "," Água  salgada, alma levada. "," Paz interior e mais amor. "," Não  preciso e ninguém fingindo que gosta de mim. "," Reza a lenda que a gente nasceu pra a feliz."," Amor próprio não  é  egoísmo,  é  necessidade."," Ela é  do tipo que tem mil personalidades em apenas um minuto."," Não diga que o céu  é o limite, quando há  pegadad na lua. ","Ou some ou soma, deixa de drama, eu ja to cansado de arrisca.","Só fique preso no que te liberta. "," Foda se o que tu pensa de mim, minha consciência de limpa parceiro."," A vida é como a Cinderela, um dia você é pisada e no outro você pisa. "," Me trocou pra curtir as festas com seu amigo e ele te trocou pra ficar comigo."," Bonita a sua nova namorada, pena que eu sou MARAVILHOSA. "," O que ele tem que eu não tenho? "," Seus olhos são meu paraiso, seu sorriso minha cocaina e seu beijo meu brigadeiro. "," Para de bobeira e vem ficar comigo. "," Gosto do som do mar, da noite e da brisa leve. "," Você partiu meu coração, mas não vou ficar no chão. "," Gosto de ficar sozinha, mas odeio me sentir sozinha. "," Se não era pra ser, fazer o que. "," Criei então um universo perfeito, feito pra nós dois ! "," Você sonhava acordada, um jeito de não sentir dor, prendia o choro e aguava o bom do amor "] 
		valor = randint(0, 100)
		resposta = choice(list)
		bot.reply_to(m, "*{}*".format(resposta), parse_mode='Markdown')

@bot.callback_query_handler(func=lambda call: True)
def test_callback(call):
    if call.data == "create_post":
        bot.answer_callback_query(call.id, "Criando postagem!")
        post = model.Post()
        post_dict[call.message.chat.id] = post
        msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text="Criando postagem. Enviar uma Frase Sera Postada No Canal @DextyOficial 📝😻.")
        bot.register_next_step_handler(msg, process_word_name)
    if call.data == "add_definition":
        bot.answer_callback_query(call.id, "Adicionando definição!")
        post = post_dict[call.message.chat.id]
        word = post.words[-1]
        definition_number = len(word.definitions) + 1
        msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text="Criando definição {0}.Enviar definição.".format(definition_number))
        bot.register_next_step_handler(msg, process_adding_definition)
    if call.data == "add_synonyms":
        bot.answer_callback_query(call.id, "Adicionando sinônimos!")
        msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text="Adicione alguns sinônimos neste formato: sinônimo, sinônimo, sinônimo.")
        bot.register_next_step_handler(msg, process_synonyms)
    if call.data == "add_tags":
        bot.answer_callback_query(call.id, "Adicionando tags!")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Adicionando tags!")
        msg = bot.send_message(chat_id=call.message.chat.id, text='Escolha um conjunto de tags nas opções abaixo.',
                               reply_markup=tags_markup(call.message))
        bot.register_next_step_handler(msg, process_adding_tags)
    if call.data == "add_links":
        bot.answer_callback_query(call.id, "Adicionando links!")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Adicionando links!")
        msg = bot.send_message(chat_id=call.message.chat.id, text='Adicionar link para Oxford Dictionary! Você pode pular '
                                                                  'pressionando o botão "Pular"', reply_markup=skip_markup())
        bot.register_next_step_handler(msg, process_adding_links_oxford)
    if call.data == "add_new_word":
        bot.answer_callback_query(call.id, "Adicionando nova palavra!")
        msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text="Adicionando nova palavra! Enviar palavra para postagem de vocabulário.")
        bot.register_next_step_handler(msg, process_word_name)
    if call.data == "cancel":
        bot.answer_callback_query(call.id, "[ ❎ ] Cancelando a criação da postagem!")
        post_dict.pop(call.message.chat.id)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="📝Crie uma nova postagem aqui.", reply_markup=main_menu_markup())
    if call.data == "finish":
        bot.answer_callback_query(call.id, "[ ❓ ] Esta é a sua postagem!")
        post = post_dict[call.message.chat.id]
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=post.print_post(), parse_mode="Markdown")
        links = post.print_links()
        if links:
            bot.send_message(call.message.chat.id, links, parse_mode="Markdown")
        bot.send_message(call.message.chat.id, "Você pode enviar essas postagens para o armazenamento ou editá-las manualmente e depois "
                                               "Envie isto. Pressione o botão 'Cancelar' para não fazer isso.",
                         reply_markup=send_to_storage_markup())
    if call.data == "send_to_storage":
        bot.answer_callback_query(call.id, "[ ⬇️ ] Enviando para armazenamento!")
        post = post_dict[call.message.chat.id]
        bot.send_message(storage_channel_id, post.print_post(), parse_mode="Markdown")
        links = post.print_links()
        if links:
            bot.send_message(storage_channel_id, links, parse_mode="Markdown")
        post_dict.pop(call.message.chat.id)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="📝Crie uma nova postagem aqui.", reply_markup=main_menu_markup())
    if call.data == "edit_before_sending":
        bot.answer_callback_query(call.id, "Editando!")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text="[ 📝 ] Envie a postagem editada manualmente aqui.")
        post = post_dict[call.message.chat.id]
        msg = bot.send_message(call.message.chat.id, post.print_post())
        bot.register_next_step_handler(msg, process_edited_post)
    if call.data == "cancel_sending_to_storage":
        post_dict.pop(call.message.chat.id)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="📝Crie uma nova postagem aqui.", reply_markup=main_menu_markup())


def process_word_name(message):
    word_name = message.text
    word_name = word_name.capitalize()
    post = post_dict[message.chat.id]
    new_word = model.Word(word_name)
    post.words.append(new_word)
    post_dict[message.chat.id] = post
    msg = bot.send_message(message.chat.id, 'Envie Seu Usuário exemplo : @DextyOficial [ Pos o Envio da um Click em [OK]"', 
    reply_markup=skip_markup())
    bot.register_next_step_handler(msg, process_part_of_speech)


def process_phonetic_transcription(message):
    if message.text != '[OK]':
        phonetic_transcription = message.text
        characters_to_replace = ['/', '\\', '[', ']']
        for char in characters_to_replace:
            phonetic_transcription = phonetic_transcription.replace(char, '')
        post = post_dict[message.chat.id]
        word = post.words[-1]
        word.phoneticTranscription = phonetic_transcription
        post_dict[message.chat.id] = post

    msg = bot.send_message(message.chat.id, "Escolha parte do discurso entre as opções abaixo.",
                           reply_markup=parts_of_speech_markup())
    bot.register_next_step_handler(msg, process_part_of_speech)


def process_part_of_speech(message):
    part_of_speech = message.text
    post = post_dict[message.chat.id]
    word = post.words[-1]
    word.partOfSpeech = part_of_speech
    post_dict[message.chat.id] = post
    bot.send_message(message.chat.id, post.print_post(), reply_markup=post_markup(message), parse_mode="Markdown")


def process_synonyms(message):
    synonyms = message.text
    post = post_dict[message.chat.id]
    word = post.words[-1]
    word.synonyms = synonyms
    post_dict[message.chat.id] = post
    bot.send_message(message.chat.id, post.print_post(), reply_markup=post_markup(message), parse_mode="Markdown")


def process_adding_definition(message):
    definition = message.text
    new_definition = model.Definition(definition)
    post = post_dict[message.chat.id]
    word = post.words[-1]
    word.definitions.append(new_definition)
    post_dict[message.chat.id] = post
    msg = bot.send_message(message.chat.id, "Adicione alguns exemplos. Cada exemplo deve começar de uma nova linha!")
    bot.register_next_step_handler(msg, process_adding_definition_examples)


def process_adding_definition_examples(message):
    definition_examples = message.text
    definition_examples_array = definition_examples.split("\n")
    post = post_dict[message.chat.id]
    word = post.words[-1]
    definition = word.definitions[-1]
    definition.examples = definition_examples_array
    post_dict[message.chat.id] = post
    bot.send_message(message.chat.id, post.print_post(), reply_markup=post_markup(message), parse_mode="Markdown")


def process_adding_tags(message):
    tags = message.text
    post = post_dict[message.chat.id]
    post.hashTags = tags
    post_dict[message.chat.id] = post
    bot.send_message(message.chat.id, post.print_post(), reply_markup=post_markup(message), parse_mode="Markdown")


def process_adding_links_oxford(message):
    if message.text != "↔️ Pular":
        link = message.text
        post = post_dict[message.chat.id]
        post.oxford = link
        post_dict[message.chat.id] = post

    msg = bot.send_message(message.chat.id, 'Adicionar link para Cambridge Dictionary! Você pode pular pressionando o botão "Pular"',
                           reply_markup=skip_markup())
    bot.register_next_step_handler(msg, process_adding_links_cambridge)


def process_adding_links_cambridge(message):
    if message.text != "↔️ Pular":
        link = message.text
        post = post_dict[message.chat.id]
        post.cambridge = link
        post_dict[message.chat.id] = post

    msg = bot.send_message(message.chat.id, 'Adicionar link para Context Reverso! Você pode pular pressionando o botão "Pular"',
                           reply_markup=skip_markup())
    bot.register_next_step_handler(msg, process_adding_links_context)


def process_adding_links_context(message):
    post = post_dict[message.chat.id]
    if message.text != "↔️ Pular":
        link = message.text
        post.context = link
        post_dict[message.chat.id] = post

    bot.send_message(message.chat.id, post.print_post(), reply_markup=post_markup(message), parse_mode="Markdown")


def process_edited_post(message):
    post = post_dict[message.chat.id]
    post_edited = message.text
    bot.send_message(storage_channel_id, post_edited, parse_mode="Markdown")
    links = post.print_links()
    if links:
        bot.send_message(storage_channel_id, links, parse_mode="Markdown")
    post_dict.pop(message.chat.id)
    bot.send_message(message.chat.id, "📝Crie uma nova postagem aqui.", reply_markup=main_menu_markup())


if __name__ == "__main__":
    bot.polling(none_stop=True)
