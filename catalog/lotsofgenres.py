from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Genre, Base, Subgenre, User

engine = create_engine('sqlite:///musicgenrewithusers.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

User1 = User(name="Blake Walters", email="Bawalters6@gmail.com")
session.add(User1)
session.commit()

myFirstGenre = Genre(user_id=1, name="Rock")

session.add(myFirstGenre)
session.commit()

posthardcore = Subgenre(user_id=1, name="Post Hardcore", description="a punk rock music genre that maintains the aggression and intensity of hardcore punk but emphasizes a greater degree of creative expression initially inspired by post-punk and noise rock.",
                    instruments="Electric Guitars, Bass Guitars, Drums", popular_years="1980-2010", genre=myFirstGenre)

session.add(posthardcore)
session.commit()

punk = Subgenre(user_id=1, name="Punk", description="is a rock music genre that developed in the early to mid-1970s in the United States, United Kingdom, and Australia. Rooted in 1960s garage rock and other forms of what is now known as 'proto-punk' music, punk rock bands rejected perceived excesses of mainstream 1970s rock. Punk bands typically produced short or fast-paced songs, with hard-edged melodies and singing styles, stripped-down instrumentation, and often political, anti-establishment lyrics.",
                    instruments="Electric Guitars, Bass Guitars, Drums", popular_years="1970-1999", genre=myFirstGenre)

session.add(punk)
session.commit()

indierock = Subgenre(user_id=1, name="Indie Rock", description="a genre of alternative rock that originated in the United States and the United Kingdom in the 1980s. Originally 'Indie' meant independent record labels and the music they produced. Indie was often used interchangeably with alternative rock. As grunge and punk revival bands in the US, and then Britpop bands in the UK, broke into the mainstream in the 1990s, indie identified those acts that retained an outsider and underground perspective.",
                    instruments="Electric Guitars, Bass Guitars, Synthesizers, Drums", popular_years="1990-present", genre=myFirstGenre)

session.add(indierock)
session.commit()

deathmetal = Subgenre(user_id=1, name="Death Metal", description="an extreme subgenre of heavy metal music. It typically employs heavily distorted and low-tuned guitars, played with techniques such as palm muting and tremolo picking, deep growling vocals, aggressive, powerful drumming featuring double kick or blast beat techniques, minor keys or atonality, abrupt tempo, key, and time signature changes and chromatic chord progressions.",
                    instruments="Electric Guitars, Bass Guitars, Drums", popular_years="1981-present", genre=myFirstGenre)

session.add(deathmetal)
session.commit()

alternativerock = Subgenre(user_id=1, name="Alternative Rock", description="is a style of rock music that emerged from the independent music underground of the 1980s and became widely popular in the 1990s. In this instance, the word 'alternative' refers to the genre's distinction from mainstream rock music.",
                    instruments="Electric Guitars, Bass Guitars, Synthesizers, Drums", popular_years="1990s", genre=myFirstGenre)

session.add(alternativerock)
session.commit()

poprock = Subgenre(user_id=1, name="Pop Rock", description="is rock music with a lighter, smoother approach that is more reminiscent of commercial pop music. Originating in the 1950s as an alternative to rock and roll, early pop rock was influenced by the beat, arrangements, and style of rock and roll (and sometimes doo-wop), but placed a greater emphasis on professional songwriting and recording craft.",
                    instruments="Electric Guitars, Bass Guitars, Synthesizers, Drums", popular_years="1980-present", genre=myFirstGenre)

session.add(poprock)
session.commit()

mySecondGenre = Genre(user_id=1, name="Rap")

session.add(mySecondGenre)
session.commit()

hiphop = Subgenre(user_id=1, name="Hip Hop", description="a subculture and art movement developed in South Bronx in New York City during the late 1970s. While the term hip hop is often used to refer exclusively to hip hop music (also called rap), hip hop is characterized by nine elements, of which hip hop music is only four elements (rapping, djaying, beatboxing and breaking).",
                    instruments="Synthesizers, Record Players, Dj Equipment", popular_years="1970s-1990s", genre=mySecondGenre)

session.add(hiphop)
session.commit()

westcoast = Subgenre(user_id=1, name="West Coast", description="a hip hop music subgenre that encompasses any artists or music that originate in the West Coast region of the United States",
                    instruments="Synthesizers, Record Players, Dj Equipment", popular_years="1980-Present", genre=mySecondGenre)

session.add(westcoast)
session.commit()

eastcoast = Subgenre(user_id=1, name="East Coast", description="a regional subgenre of hip hop music that originated in the New York City area during the 1970s",
                    instruments="Synthesizers, Record Players, Dj Equipment", popular_years="1970s-1990s", genre=mySecondGenre)

session.add(eastcoast)
session.commit()

gangsta = Subgenre(user_id=1, name="Gangsta", description="a subgenre of hip hop music with themes and lyrics that generally emphasize the 'gangsta' lifestyle. The genre evolved from hardcore hip hop into a distinct form, pioneered in the mid-1980s by rappers such as Schoolly D and Ice-T, and was popularized in the later part of the 1980s by groups like N.W.A.",
                    instruments="Synthesizers, Record Players, Dj Equipment", popular_years="1980s-Present", genre=mySecondGenre)

session.add(gangsta)
session.commit()

myThirdGenre = Genre(user_id=1, name="Jazz")

session.add(myThirdGenre)
session.commit()

acid = Subgenre(user_id=1, name="Acid", description="also known as club jazz, is a musical genre that combines elements of jazz, soul, funk, and disco.",
                    instruments="Synthesizers, Saxophones, Flutes, Trumpets, Trombones, Clarinets, Pianos, Guitars, Bass, Drums, Strings, Organs", popular_years="1980s-2000s", genre=myThirdGenre)

session.add(acid)
session.commit()

avantgarde = Subgenre(user_id=1, name="Avant-Garde", description="a style of music and improvisation that combines avant-garde art music and composition with jazz.",
                    instruments="Synthesizers, Saxophones, Flutes, Trumpets, Trombones, Clarinets, Pianos, Guitars, Bass, Drums, Strings, Organs", popular_years="1950s-1960s", genre=myThirdGenre)

session.add(avantgarde)
session.commit()

contemporary = Subgenre(user_id=1, name="Contemporary", description="Jazz music of the current time frame",
                    instruments="Horns, Keyboards, Bass, Drums, Guitars", popular_years="Present", genre=myThirdGenre)

session.add(contemporary)
session.commit()

bigband = Subgenre(user_id=1, name="Big Band", description="a type of musical ensemble that usually consists of ten or more musicians with four sections: saxophones, trumpets, trombones, and a rhythm section. Big bands originated during the early 1910s and dominated jazz through the 1940s",
                    instruments="Saxophones, Trumpets, Trombones, Rhythm Section", popular_years="1910-1940s", genre=myThirdGenre)

session.add(bigband)
session.commit()

myFourthGenre = Genre(user_id=1, name="Classical")

session.add(myFourthGenre)
session.commit()

baroque = Subgenre(user_id=1, name="Baroque", description="is a style of Western art music composed from approximately 1600 to 1750. This era followed the Renaissance music era, and was followed in turn by the Classical era. Baroque music forms a major portion of the classical music canon, being nowadays widely studied, performed, and listened to.",
                    instruments="Orchestral", popular_years="1600-1750", genre=myFourthGenre)

session.add(baroque)
session.commit()

impressionist = Subgenre(user_id=1, name="Impressionist", description="a movement among various composers in Western classical music, mainly during the late 19th and early 20th centuries, whose music focuses on suggestion and atmosphere, conveying the moods and emotions aroused by the subject rather than a detailed tone picture.",
                    instruments="Orchestral", popular_years="1875-1925", genre=myFourthGenre)

session.add(impressionist)
session.commit()

minimalism = Subgenre(user_id=1, name="Minimalism", description="a form of art music that employs limited or minimal musical materials. In the Western art music tradition the American composers La Monte Young, Terry Riley, Steve Reich, and Philip Glass are credited with being among the first to develop compositional techniques that exploit a minimal approach.",
                    instruments="Orchestral", popular_years="1940s-1960s", genre=myFourthGenre)

session.add(minimalism)
session.commit()

romantic = Subgenre(user_id=1, name="Romantic", description="a period of Western classical music that began in the late 18th or early 19th century. It is related to Romanticism, the European artistic and literary movement that arose in the second half of the 18th century, and Romantic music in particular dominated the Romantic movement in Germany.",
                    instruments="Orchestral", popular_years="1780-1910", genre=myFourthGenre)

session.add(romantic)
session.commit()

myFifthGenre = Genre(user_id=1, name="Blues")

session.add(myFifthGenre)
session.commit()

boogiewoogie = Subgenre(user_id=1, name="Boogie Woogie", description="a musical genre that became popular during the late 1920s, but developed in African American communities in the 1870s. It was eventually extended from piano, to piano duo and trio, guitar, big band, country and western music, and gospel. While the blues traditionally expresses a variety of emotions, boogie-woogie is mainly associated with dancing.",
                    instruments="Pianos", popular_years="1920s", genre=myFifthGenre)

session.add(boogiewoogie)
session.commit()

bluesrock = Subgenre(user_id=1, name="Blues Rock", description="a fusion genre combining elements of blues and rock. It is mostly an electric ensemble-style music with instrumentation similar to electric blues and rock: electric guitar, electric bass, and drums, often with Hammond organ.",
                    instruments="Drums, Electirc Guitars, Bass Guitars, Hammond Organs, Pianos, Harmonicas", popular_years="1960s-Present", genre=myFifthGenre)

session.add(bluesrock)
session.commit()

detroitblues = Subgenre(user_id=1, name="Detroit Blues", description="blues played by musicians residing in and around Detroit, Michigan, particularly in the 1940s and 1950s. Detroit blues originated when Delta blues performers migrated north from the Mississippi Delta and Memphis, Tennessee, to work in industrial plants in Detroit in the 1920s and 1930s.",
                    instruments="Electric Guitars, Harmonicas, Drums, Pianos, Bass Guitars, Saxophones", popular_years="1940s-1950s", genre=myFifthGenre)

session.add(detroitblues)
session.commit()

dirtyblues = Subgenre(user_id=1, name="Dirty Blues", description="encompasses forms of blues music that deal with socially taboo subjects, including sexual acts and/or references to drug use of some kind. Due to the sometimes graphic subject matter, such music was often banned from radio and only available on a jukebox. The style was most popular in the years before World War II, although it had a revival in the 1960s.",
                    instruments="Electric Guitars, Harmonicas, Drums, Pianos, Bass Guitars, Saxophones", popular_years="1930s-1960s", genre=myFifthGenre)

session.add(dirtyblues)
session.commit()

mySixthGenre = Genre(user_id=1, name="Reggae")

session.add(mySixthGenre)
session.commit()

mento = Subgenre(user_id=1, name="Mento", description="a style of Jamaican folk music that predates and has greatly influenced ska and reggae music. Mento typically features acoustic instruments, such as acoustic guitar, banjo, hand drums, and the rhumba box, a large mbira in the shape of a box that can be sat on while played. The rhumba box carries the bass part of the music.",
                    instruments="Acooustic Guitars, Bongo Drums, Banjos, Hand Drums, Marimbulas", popular_years="1960s", genre=mySixthGenre)

session.add(mento)
session.commit()

jamaicanreggae = Subgenre(user_id=1, name="Jamaican Reggae", description="includes Jamaican folk music and many popular genres, such as mento, ska, rocksteady, reggae, dub music, dancehall, ska jazz, reggae fusion and related styles. Jamaica's music culture is a fusion of elements from neighboring Caribbean islands such as Trinidad and Tobago (calypso and soca).",
                    instruments="Electric Guitars, Bass Guitars, Drums, Horns, Organs", popular_years="1960s-1970s", genre=mySixthGenre)

session.add(jamaicanreggae)
session.commit()

rocksteady = Subgenre(user_id=1, name="Rock Steady", description="musical genre, a predecessor of reggae, that was most popular in Jamaica in the 1960s",
                    instruments="Electric Guitars, Bass Guitars, Drums, Horns, Organs", popular_years="1960s", genre=mySixthGenre)

session.add(rocksteady)
session.commit()

dancehall = Subgenre(user_id=1, name="Dancehall", description="a genre of Jamaican popular music that originated in the late 1970s. Initially, dancehall was a more sparse version of reggae than the roots style, which had dominated much of the 1970s.",
                    instruments="Drums, Bass Guitars, Electric Guitars, Electronic Organs", popular_years="1970s-1980s", genre=mySixthGenre)

session.add(dancehall)
session.commit()

dub = Subgenre(user_id=1, name="Dub", description="grew out of reggae in the 1960s, and is commonly considered a subgenre, though it has developed to extend beyond the scope of reggae. Music in this genre consists predominantly of instrumental remixes of existing recordings",
                    instruments="Bass Guitars, Drums, Guitars, Electronic Organs, Brass Instruments, Synthesizers, Melodicas, Mixing Consoles", popular_years="1960s-1980s", genre=mySixthGenre)

session.add(dub)
session.commit()

mySeventhGenre = Genre(user_id=1, name="Latin")

session.add(mySeventhGenre)
session.commit()

salsa = Subgenre(user_id=1, name="Salsa", description="a popular dance music that initially arose in New York City during the 1960s. Salsa is the product of various musical genres including the Cuban son montuno, guaracha, cha cha cha, mambo, and to a certain extent bolero, and the Puerto Rican bomba and plena.",
                    instruments="Pianos, Bongos, Congas, Timbales, Trumpets, Trombones, Claves, Cowbells, Maracas, Guiros, Bass Guitars, Guitars, Saxophones, Vibraphones", popular_years="1960s-1970s", genre=mySeventhGenre)

session.add(salsa)
session.commit()

bossanova = Subgenre(user_id=1, name="Bossa Nova", description="a genre of Brazilian music, which developed and was popularized in the 1950s and 1960s and is today one of the best-known Brazilian music genres abroad.",
                    instruments="Classical Guitars, Acoustic Guitars, Pianos, Electric Organs, Acoustic Bass, Drums", popular_years="1950s-1960s", genre=mySeventhGenre)

session.add(bossanova)
session.commit()

samba = Subgenre(user_id=1, name="Samba", description="a Brazilian musical genre and dance style, with its roots in Africa via the West African slave trade and African religious traditions, particularly of Angola and the Congo, through the samba de roda genre of the northeastern Brazilian state of Bahia, from which it derived.",
                    instruments="Cavaquinhos, Tamborims", popular_years="1910s-1920s", genre=mySeventhGenre)

session.add(samba)
session.commit()

boogaloo = Subgenre(user_id=1, name="Boogaloo", description="a genre of Latin music and dance which was popular in the United States in the 1960s. Boogaloo originated in New York City mainly among teenage Puerto Ricans. The style was a fusion of popular African American rhythm and blues (R&B) and soul music with mambo and son montuno, with songs in both English and Spanish.",
                    instruments="Trombones, Pianos, Congas, Trumpets, Bass Guitars, Double Bass, Electric Guitars, Bongos, Saxophones, Guiros, Timbales", popular_years="1960s", genre=mySeventhGenre)

session.add(boogaloo)
session.commit()

print "add genres!"

