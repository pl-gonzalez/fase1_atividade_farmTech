lavouras <- read.csv("C:/Users/Automação/Desktop/Coding/fiap/FarmTech/fase1_atividade_farmTech/output.csv")

media_area = mean(lavouras$area)
mediana_area = median(lavouras$area)
desvio_area = sd(lavouras$area)

media_qtd_insumo = mean(lavouras$qnt_insumo)
mediana_qtd_insumo = median(lavouras$qnt_insumo)
desvio_qtd_insumo = sd(lavouras$qnt_insumo)

media_ins_litros = mean(lavouras$qnt_litros)
mediana_ins_litros = median(lavouras$qnt_litros)
desvio_ins_litros = sd(lavouras$qnt_litros)

media_ruas = mean(lavouras$ruas)
mediana_ruas = median(lavouras$ruas)
desvio_ruas = sd(lavouras$ruas)

cat(
  "\n\nA media da área é ",  media_area," m²",
  "\nA mediana da área é: ", mediana_area, " m²",
  "\nO desvio da área é: ", desvio_area, " m²"
)
cat(
  "\n\nA media da quantidade de insumo, em litros, é ",  media_ins_litros, "L",
  "\nA mediana da quantidade de insumo, em litros, é: ", mediana_ins_litros,"L",
  "\nO desvio da quantidade de insumo, em litros, é: ", desvio_ins_litros,"L"
)
cat(
  "\n\nA media da quantidade de ruas é ",  media_ruas,
  "\nA mediana da quantidade de ruas é: ", mediana_ruas,
  "\nO desvio da quantidade de ruas é: ", desvio_ruas
)





