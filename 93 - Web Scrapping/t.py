from bs4 import BeautifulSoup

#ESTE ERA HTML LE CAMBIE EL NOMBRE POR Points
Points = '<div class="LeaderBoardCard_lbcWrapper__e4bCZ LeaderBoardWithButtons_lbwbCardGrid__Iqg6m LeaderBoardCard_leaderBoardCategory__vWRuZ"><h2 class="LeaderBoardCard_lbcTitle___WI9J">Points</h2><hr class="LeaderBoardCard_lbcHr__UDY9r"><div class="LeaderBoardPlayerCard_lbpc__UG8WY" data-show-padding="true" data-show-team="true"><table class="LeaderBoardPlayerCard_lbpcTable__q3iZD"><tbody><tr class="LeaderBoardPlayerCard_lbpcTableRow___Lod5"><td class="LeaderBoardPlayerCard_lbpcTableCell__SnM1o">1<!-- -->. </td><td><a href="/stats/player/203999/" class="Anchor_anchor__cSc3P LeaderBoardPlayerCard_lbpcTableLink__MDNgL" data-is-external="false" data-has-more="false" data-has-children="false">Nikola Jokic</a><span class="LeaderBoardPlayerCard_lbpcTeamAbbr__fGlx3">DEN</span></td><td class="LeaderBoardWithButtons_lbwbCardValue__5LctQ"><a href="/game/0042200405/box-score" class="Anchor_anchor__cSc3P LeaderBoardPlayerCard_lbpcTableLink__MDNgL" data-is-external="false" data-has-more="false" data-has-children="false">28</a></td></tr><tr class="LeaderBoardPlayerCard_lbpcTableRow___Lod5"><td class="LeaderBoardPlayerCard_lbpcTableCell__SnM1o">2<!-- -->. </td><td><a href="/stats/player/202710/" class="Anchor_anchor__cSc3P LeaderBoardPlayerCard_lbpcTableLink__MDNgL" data-is-external="false" data-has-more="false" data-has-children="false">Jimmy Butler</a><span class="LeaderBoardPlayerCard_lbpcTeamAbbr__fGlx3">MIA</span></td><td class="LeaderBoardWithButtons_lbwbCardValue__5LctQ"><a href="/game/0042200405/box-score" class="Anchor_anchor__cSc3P LeaderBoardPlayerCard_lbpcTableLink__MDNgL" data-is-external="false" data-has-more="false" data-has-children="false">21</a></td></tr><tr class="LeaderBoardPlayerCard_lbpcTableRow___Lod5"><td class="LeaderBoardPlayerCard_lbpcTableCell__SnM1o">3<!-- -->. </td><td><a href="/stats/player/1628389/" class="Anchor_anchor__cSc3P LeaderBoardPlayerCard_lbpcTableLink__MDNgL" data-is-external="false" data-has-more="false" data-has-children="false">Bam Adebayo</a><span class="LeaderBoardPlayerCard_lbpcTeamAbbr__fGlx3">MIA</span></td><td class="LeaderBoardWithButtons_lbwbCardValue__5LctQ"><a href="/game/0042200405/box-score" class="Anchor_anchor__cSc3P LeaderBoardPlayerCard_lbpcTableLink__MDNgL" data-is-external="false" data-has-more="false" data-has-children="false">20</a></td></tr><tr class="LeaderBoardPlayerCard_lbpcTableRow___Lod5"><td class="LeaderBoardPlayerCard_lbpcTableCell__SnM1o">4<!-- -->. </td><td><a href="/stats/player/1629008/" class="Anchor_anchor__cSc3P LeaderBoardPlayerCard_lbpcTableLink__MDNgL" data-is-external="false" data-has-more="false" data-has-children="false">Michael Porter Jr.</a><span class="LeaderBoardPlayerCard_lbpcTeamAbbr__fGlx3">DEN</span></td><td class="LeaderBoardWithButtons_lbwbCardValue__5LctQ"><a href="/game/0042200405/box-score" class="Anchor_anchor__cSc3P LeaderBoardPlayerCard_lbpcTableLink__MDNgL" data-is-external="false" data-has-more="false" data-has-children="false">16</a></td></tr><tr class="LeaderBoardPlayerCard_lbpcTableRow___Lod5"><td class="LeaderBoardPlayerCard_lbpcTableCell__SnM1o">5<!-- -->. </td><td><a href="/stats/player/1627750/" class="Anchor_anchor__cSc3P LeaderBoardPlayerCard_lbpcTableLink__MDNgL" data-is-external="false" data-has-more="false" data-has-children="false">Jamal Murray</a><span class="LeaderBoardPlayerCard_lbpcTeamAbbr__fGlx3">DEN</span></td><td class="LeaderBoardWithButtons_lbwbCardValue__5LctQ"><a href="/game/0042200405/box-score" class="Anchor_anchor__cSc3P LeaderBoardPlayerCard_lbpcTableLink__MDNgL" data-is-external="false" data-has-more="false" data-has-children="false">14</a></td></tr></tbody></table></div></div>'


# Creamos un objeto BeautifulSoup para analizar el HTML
soup = BeautifulSoup(Points, 'html.parser')

# Encontramos el título de la tabla (por ejemplo, 'Points')
table_title = soup.find('h2', class_='LeaderBoardCard_lbcTitle___WI9J').text.strip()
print(f'Título de la tabla: {table_title}')

# Encontramos todas las filas de la tabla
rows = soup.find_all('tr', class_='LeaderBoardPlayerCard_lbpcTableRow___Lod5')

# Recorremos cada fila y extraemos los datos
for row in rows:
    # Obtenemos el puesto
    position = row.find('td', class_='LeaderBoardPlayerCard_lbpcTableCell__SnM1o')
    position = position.text.strip() if position else "N/A"

    # Obtenemos el nombre del jugador y el equipo
    player_name = row.find('a', class_='LeaderBoardPlayerCard_lbpcTableLink__MDNgL')
    player_name = player_name.text.strip() if player_name else "N/A"

    team = row.find('span', class_='LeaderBoardPlayerCard_lbpcTeamAbbr__fGlx3')
    team = team.text.strip() if team else "N/A"

    # Obtenemos los puntos del jugador
    points_container = row.find('td', class_='LeaderBoardWithButtons_lbwbCardValue__5LctQ')
    points = points_container.find('a').text.strip() if points_container else "N/A"

    # Mostramos los datos en consola
    print(f'{position}. {player_name} ({team}): {points}')
