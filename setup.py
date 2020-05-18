from distutils.core import setup
setup(
    name='pgn2bitboard',         # How you named your package folder (MyLib)
    packages=['pgn2bitboard'],   # Chose the same as "name"
    version='0.2',      # Start with a small number and increase it with every change you make
    # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    license='MIT',
    # Give a short description about your library
    description='This library is used to process pgn files that contain several chess games and convert them to bitboards and labels.',
    author='Anirudh',                   # Type in your name
    author_email='anirudhganwal06@gmail.com',      # Type in your E-Mail
    # Provide either the link to your github or to your website
    url='https://github.com/anirudhganwal06/pgn2bitboard',
    # I explain this later on
    download_url='https://github.com/anirudhganwal06/pgn2bitboard/archive/v0.2.tar.gz',
    # Keywords that define your package best
    keywords=['pgn', 'bitboard', 'chess', 'chess-engine'],
    install_requires=[            # I get to this in a second
        'numpy',
        'python-chess'
    ],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 3 - Alpha',
        # Define that your audience are developers
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        # Specify which python versions that you want to support
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
