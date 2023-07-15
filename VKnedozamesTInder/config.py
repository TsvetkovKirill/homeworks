user_token = ''  # токен пользователя
# access_token = 'vk1.a.IkmCS3TFwP6TqGJRkq4Ca_cW930zDn4H5nGMp3LLgk_nOnYmdP8VZyOn3F1FhUSZlrPiLfwo8zHTJfeRQqcSapdwugt0R0yyB0CAMYhkf2mBtCecOPEoUHHg3go7lUKUBi00adSlc5IooOZpbdTLxdbh0ua--HbZkNn3BMtpnw2Z_D3UcvkEn7kEuqaEQIWU_FnmiP-skENn0Jrhqhal5g'
bot_key = 'vk1.a.D7HzFlLFr0N1rwxmRz6UfyTDM1yLlnoQoMi5eWf-_3jCg4MKFYOMV2MSdwRrVNhO-TEozZCMnAloY4h6hx3dLDMtt3Oo-SLixbJly1hmVt8ZdppbZ_Btc3O1bLiRcnxqRu5yqrEagzsDhQx3AFLS-1e5ogdJ737y2PR8us0WHz_j0UJtQhINUOT1gD1EvmHmq2PQgdO-8EC7tjKMhPQk4A'
# service_key_access = '1b1f81ca1b1f81ca1b1f81caec180b563d11b1f1b1f81ca7fb869370890bfe2f63e8eec'

offset = 0  # сдвиг
line = range(0, 1000)  # последовательность для перебора найденных пользователей
mask = 248661618204893321077691124073410420050228075398673858720231988446579748506266688011743
host = '127.0.0.1'
user = 'postgres'
password = '0000'
db_name = 'bot_users'
link_get_token = 'https://oauth.vk.com/authorize?client_id=51697655&display=page&redirect_uri=https://vk.com/away.php?to=https://oauth.vk.com/blank.html&scope=248661618204893321077691124073410420050228075398673858720231988446579748506266688011743&response_type=token&v=5.131&state=123456'