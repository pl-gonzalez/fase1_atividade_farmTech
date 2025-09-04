lavouras <- data.frame(
  cultura = c("cafe", "milho", "soja", "cana-de-açucar", "laranja"),
  comprimento = c(250, 350, 550, 500, 600),
  largura = c(450, 650, 950, 600, 760),
  area = c(112500, 227500, 522500, 300000, 456000),
  insumo = c("fosfato", "fosfato", "fosfato", "fosfato", "fosfato"),
  qtd_insumo = c(120, 100, 180, 200, 90),
  ins_litros = c(13500, 22750, 94050, 60000, 41040),
  ruas = c(40, 55, 68, 74, 63)
)

media_area = mean(lavouras$area)
mediana_area = median(lavouras$area)
desvio_area = sd(lavouras$area)

media_qtd_insumo = mean(lavouras$qtd_insumo)
mediana_qtd_insumo = median(lavouras$qtd_insumo)
desvio_qtd_insumo = sd(lavouras$qtd_insumo)

media_ins_litros = mean(lavouras$ins_litros)
mediana_ins_litros = median(lavouras$ins_litros)
desvio_ins_litros = sd(lavouras$ins_litros)

media_ruas = mean(lavouras$ruas)
mediana_ruas = median(lavouras$ruas)
desvio_ruas = sd(lavouras$ruas)