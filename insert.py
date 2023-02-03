import sqlite3 as sql

con = sql.connect('region.db')
cursor = con.cursor()
cursor.execute("""INSERT INTO USER(region, client, link) VALUES
("kz", "mechta", "https://www.mechta.kz/product/telefon-sotovyy-honor-x8-6128gb-titanium-silver/"),
("kz", "mechta", "https://www.mechta.kz/product/telefon-sotovyy-samsung-sm-a-235-galaxy-a23-64gb-fzkus-black/"),
("kz", "mechta", "https://www.mechta.kz/product/telefon-sotovyy-samsung-sm-a-235-galaxy-a23-128gb-fzkks-black/"),
("kz", "mechta", "https://www.mechta.kz/product/telefon-sotovyy-vivo-y35-464gb-dawn-gold-v2205/"),
("kz", "mechta", "https://www.mechta.kz/product/telefon-sotovyy-vivo-y35-4128gb-dawn-gold-v2205/"),
("kz", "mechta", "https://www.mechta.kz/product/telefon-sotovyy-vivo-y53s-8128gb-fantastic-rainbow-v2058/"),
("kz", "mechta", "https://www.mechta.kz/product/telefon-sotovyy-oppo-a74-prism-black/"),
("kz", "mechta", "https://www.mechta.kz/product/telefon-sotovyy-xiaomi-redmi-note-11s-6128gb-graphite-gray/"),
("kz", "mechta", "https://www.mechta.kz/product/telefon-sotovyy-vivo-y55-12128gb-ice-dawn-v2154/"),
("kz", "mechta", "https://www.mechta.kz/product/telefon-sotovyy-honor-x9-6128gb-midnight-black/"),
("kz", "mechta", "https://www.mechta.kz/product/telefon-sotovyy-samsung-sm-a-336-galaxy-a33-5g-128gb-bzkgs-black/"),
("kz", "mechta", "https://www.mechta.kz/product/telefon-sotovyy-vivo-v23e-8128gb-moonlight-shadow-v2116/"),
("kz", "mechta", "https://www.mechta.kz/product/telefon-sotovyy-oppo-a96-6128-starry-black/"),
("kz", "mechta", "https://www.mechta.kz/product/telefon-sotovyy-xiaomi-redmi-note-11-pro-8128gb-graphite-gray/ "),
("kz", "mechta", "https://www.mechta.kz/product/telefon-sotovyy-vivo-v25e-8128gb-diamond-black-v2201/"),
("kz", "mechta", "https://www.mechta.kz/product/telefon-sotovyy-oppo-reno-7-8128gb-cosmic-black/"),
("kz", "mechta", "https://www.mechta.kz/product/telefon-sotovyy-oppo-reno-7-5g-8256gb-startrails-blue/"),
("kz", "mechta", "https://www.mechta.kz/product/telefon-sotovyy-oppo-a77s-8128gb-sunset-orange/"),
("kz", "mechta", "https://www.mechta.kz/product/telefon-sotovyy-honor-70-8256gb-emerald-green/"),
("kz", "mechta", "https://www.mechta.kz/product/telefon-sotovyy-honor-70-8128gb-emerald-green/"),
("kz", "mechta", "https://www.mechta.kz/product/telefon-sotovyy-vivo-v25-5g-8256gb-diamond-black-v2202/"),
("kz", "mechta", "https://www.mechta.kz/product/telefon-sotovyy-vivo-v25-pro-5g-12256gb-starlight-black-v2158/"),
("kz", "mechta", "https://www.mechta.kz/product/telefon-sotovyy-oppo-reno-7-5g-8256gb-starry-black/"),
("kz", "mechta", "https://www.mechta.kz/product/telefon-sotovyy-xiaomi-11t-8256gb-celestial-blue/"),
("kz", "mechta", "https://www.mechta.kz/product/telefon-sotovyy-samsung-sm-a-736-galaxy-a73-5g-6128gb-blgds-green/"),
("kz", "mechta", "https://www.mechta.kz/product/telefon-sotovyy-samsung-sm-a-736-galaxy-a73-5g-8256gb-blghs-green/"),
("kz", "mechta", "https://www.mechta.kz/product/telefon-sotovyy-samsung-sm-g-990-galaxy-s21-fe-128gb-new-bzafs-gray/");
""")
con.commit()