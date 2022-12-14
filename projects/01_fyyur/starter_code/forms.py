from datetime import datetime
from flask_wtf import Form
from wtforms import StringField, SelectField, SelectMultipleField, DateTimeField, BooleanField
from wtforms.validators import DataRequired, AnyOf, URL, Length #my additions: Length

# My edit
from enum import Enum
# My edit ends here

#impelemnting genres enum
class Genres(Enum):
    ALTERNATIVE = 'Alternative'
    BLUES = 'Blues'
    CLASSICAL = 'Classical'
    COUNTRY = 'Country'
    ELECTRONIC = 'Electronic'
    FOLK = 'Folk'
    FUNK = 'Funk'
    HIP_HOP = 'Hip-Hop'
    HEAVY_METAL = 'Heavy Metal'
    INSTRUMENTAL = 'Instrumental'
    JAZZ = 'Jazz'
    MUSICAL_THEATRE = 'Musical Theatre'
    POP ='Pop'
    PUNK = 'Punk'
    R_AND_B = 'R&B'
    REGGAE = 'Reggae'
    ROCK_N_ROLL = 'Rock n Roll'
    SOUL = 'Soul'
    OTHER = 'Other'

# Impelemnting the State enum
class States(Enum):
    AL = 'AL'
    AK = 'AK'
    AZ = 'AZ'
    AR = 'AR'
    CA = 'CA'
    CO = 'CO'
    CT = 'CT'
    DE ='DE'
    DC = 'DC'
    FL = 'FL'
    GA = 'GA'
    HI = 'HI'
    ID = 'ID'
    IL = 'IL'
    IN = 'IN'
    IA = 'IA'
    KS = 'KS'
    KY = 'KY'
    LA = 'LA'
    ME = 'ME'
    MT = 'MT'
    NE = 'NE'
    NV = 'NV'
    NH = 'NH'
    NJ = 'NJ'
    NM = 'NM'
    NY = 'NY'
    NC = 'NC'
    ND = 'ND'
    OH = 'OH'
    OK = 'OK'
    OR = 'OR'
    MD = 'MD'
    MA = 'MA'
    MI = 'MI'
    MN = 'MN'
    MS = 'MS'
    MO = 'MO'
    PA = 'PA'
    RI = 'RI'
    SC = 'SC'
    SD = 'SD'
    TN = 'TN'
    TX = 'TX'
    UT = 'UT'
    VT = 'VT'
    VA = 'VA'
    WA = 'WA'
    WV = 'WV'
    WI = 'WI'
    WY = 'WY'


class ShowForm(Form):
    artist_id = StringField(
        'artist_id'
    )
    venue_id = StringField(
        'venue_id'
    )
    start_time = DateTimeField(
        'start_time',
        validators=[DataRequired()],
        default= datetime.today()
    )

class VenueForm(Form):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    city = StringField(
        'city', validators=[DataRequired()]
    )
    state = SelectField(
        'state', validators=[DataRequired()],
        # next impelementing enum restriction
        choices=[(member.value, name.upper()) for name, member in States.__members__.items()
            # ('AL', 'AL'),
            # ('AK', 'AK'),
            # ('AZ', 'AZ'),
            # ('AR', 'AR'),
            # ('CA', 'CA'),
            # ('CO', 'CO'),
            # ('CT', 'CT'),
            # ('DE', 'DE'),
            # ('DC', 'DC'),
            # ('FL', 'FL'),
            # ('GA', 'GA'),
            # ('HI', 'HI'),
            # ('ID', 'ID'),
            # ('IL', 'IL'),
            # ('IN', 'IN'),
            # ('IA', 'IA'),
            # ('KS', 'KS'),
            # ('KY', 'KY'),
            # ('LA', 'LA'),
            # ('ME', 'ME'),
            # ('MT', 'MT'),
            # ('NE', 'NE'),
            # ('NV', 'NV'),
            # ('NH', 'NH'),
            # ('NJ', 'NJ'),
            # ('NM', 'NM'),
            # ('NY', 'NY'),
            # ('NC', 'NC'),
            # ('ND', 'ND'),
            # ('OH', 'OH'),
            # ('OK', 'OK'),
            # ('OR', 'OR'),
            # ('MD', 'MD'),
            # ('MA', 'MA'),
            # ('MI', 'MI'),
            # ('MN', 'MN'),
            # ('MS', 'MS'),
            # ('MO', 'MO'),
            # ('PA', 'PA'),
            # ('RI', 'RI'),
            # ('SC', 'SC'),
            # ('SD', 'SD'),
            # ('TN', 'TN'),
            # ('TX', 'TX'),
            # ('UT', 'UT'),
            # ('VT', 'VT'),
            # ('VA', 'VA'),
            # ('WA', 'WA'),
            # ('WV', 'WV'),
            # ('WI', 'WI'),
            # ('WY', 'WY'),
        ]
    )
    address = StringField(
        'address', validators=[DataRequired()]
    )
    phone = StringField(
        'phone',
        #my work on validation phone number is in the next line
        validators=[DataRequired(), Length(10)]
    )
    image_link = StringField(
        'image_link',
    )
    genres = SelectMultipleField(
        # TODO implement enum restriction
        'genres', validators=[DataRequired()],
        choices=[(member.value, name.capitalize()) for name, member in Genres.__members__.items()
            # ('Alternative', 'Alternative'),
            # ('Blues', 'Blues'),
            # ('Classical', 'Classical'),
            # ('Country', 'Country'),
            # ('Electronic', 'Electronic'),
            # ('Folk', 'Folk'),
            # ('Funk', 'Funk'),
            # ('Hip-Hop', 'Hip-Hop'),
            # ('Heavy Metal', 'Heavy Metal'),
            # ('Instrumental', 'Instrumental'),
            # ('Jazz', 'Jazz'),
            # ('Musical Theatre', 'Musical Theatre'),
            # ('Pop', 'Pop'),
            # ('Punk', 'Punk'),
            # ('R&B', 'R&B'),
            # ('Reggae', 'Reggae'),
            # ('Rock n Roll', 'Rock n Roll'),
            # ('Soul', 'Soul'),
            # ('Other', 'Other'),
        ]
    )
    facebook_link = StringField(
        'facebook_link', validators=[URL()]
    )
    website_link = StringField(
        'website_link', validators=[URL()] # I added validation
    )

    seeking_talent = BooleanField(
        'seeking_talent'
    )

    seeking_description = StringField(
        'seeking_description'
    )



class ArtistForm(Form):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    city = StringField(
        'city', validators=[DataRequired()]
    )
    state = SelectField(
        'state', validators=[DataRequired()],
        # next impelementing enum restriction
        choices=[(member.value, name.upper()) for name, member in States.__members__.items()
            # ('AL', 'AL'),
            # ('AK', 'AK'),
            # ('AZ', 'AZ'),
            # ('AR', 'AR'),
            # ('CA', 'CA'),
            # ('CO', 'CO'),
            # ('CT', 'CT'),
            # ('DE', 'DE'),
            # ('DC', 'DC'),
            # ('FL', 'FL'),
            # ('GA', 'GA'),
            # ('HI', 'HI'),
            # ('ID', 'ID'),
            # ('IL', 'IL'),
            # ('IN', 'IN'),
            # ('IA', 'IA'),
            # ('KS', 'KS'),
            # ('KY', 'KY'),
            # ('LA', 'LA'),
            # ('ME', 'ME'),
            # ('MT', 'MT'),
            # ('NE', 'NE'),
            # ('NV', 'NV'),
            # ('NH', 'NH'),
            # ('NJ', 'NJ'),
            # ('NM', 'NM'),
            # ('NY', 'NY'),
            # ('NC', 'NC'),
            # ('ND', 'ND'),
            # ('OH', 'OH'),
            # ('OK', 'OK'),
            # ('OR', 'OR'),
            # ('MD', 'MD'),
            # ('MA', 'MA'),
            # ('MI', 'MI'),
            # ('MN', 'MN'),
            # ('MS', 'MS'),
            # ('MO', 'MO'),
            # ('PA', 'PA'),
            # ('RI', 'RI'),
            # ('SC', 'SC'),
            # ('SD', 'SD'),
            # ('TN', 'TN'),
            # ('TX', 'TX'),
            # ('UT', 'UT'),
            # ('VT', 'VT'),
            # ('VA', 'VA'),
            # ('WA', 'WA'),
            # ('WV', 'WV'),
            # ('WI', 'WI'),
            # ('WY', 'WY'),
        ]
    )
    phone = StringField(
        # TODO implement validation logic for phone 
        'phone',
        #my work on validation is in the next line
        validators=[DataRequired(), Length(10)]
    )
    image_link = StringField(
        'image_link'
    )
    genres = SelectMultipleField(
        'genres', validators=[DataRequired()],
        choices=[(member.value, name.capitalize()) for name, member in Genres.__members__.items()
            # ('Alternative', 'Alternative'),
            # ('Blues', 'Blues'),
            # ('Classical', 'Classical'),
            # ('Country', 'Country'),
            # ('Electronic', 'Electronic'),
            # ('Folk', 'Folk'),
            # ('Funk', 'Funk'),
            # ('Hip-Hop', 'Hip-Hop'),
            # ('Heavy Metal', 'Heavy Metal'),
            # ('Instrumental', 'Instrumental'),
            # ('Jazz', 'Jazz'),
            # ('Musical Theatre', 'Musical Theatre'),
            # ('Pop', 'Pop'),
            # ('Punk', 'Punk'),
            # ('R&B', 'R&B'),
            # ('Reggae', 'Reggae'),
            # ('Rock n Roll', 'Rock n Roll'),
            # ('Soul', 'Soul'),
            # ('Other', 'Other'),
        ]
     )
    facebook_link = StringField(
        # TODO implement enum restriction
        'facebook_link', validators=[URL()]
     )

    website_link = StringField(
        'website_link', validators=[URL()] # I added validation
     )

    seeking_venue = BooleanField( 'seeking_venue' )

    seeking_description = StringField(
            'seeking_description'
     )

