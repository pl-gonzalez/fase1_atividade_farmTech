library(httr)
library(jsonlite)

# Configuração
api_key <- "c10775657c54d4b71c7c063777e988db"
cidade <- "São Paulo"
lat <- -23.5489
lon <- -46.6388
url <- paste0(
  "https://api.open-meteo.com/v1/forecast?latitude=-23.5489&longitude=-46.6388&timezone=America%2FSao_Paulo&current=temperature_2m,relative_humidity_2m,precipitation_probability,rain,cloud_cover_mid,wind_speed_10m,temperature_80m,apparent_temperature&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"

)

# Requisição para a API
resposta <- httr :: GET(url)

# str(resposta$content)

resposta_content <- httr :: content(resposta, as = "text")
# str(resposta_content)

respostaJSON = jsonlite::fromJSON(resposta_content)

# View(respostaJSON)

# print(respostaJSON$current)
temperatura = paste(
  "Temperatura Atual: ", respostaJSON$current$temperature_2m, "°C")

horas <- paste(
  "Horário: ", respostaJSON$current$time
)

umidade_rel <- paste(
  "Umidade relativa: ", respostaJSON$current$relative_humidity_2m, "%"
)

chance_chuva <- paste(
  "Chance de chuva: ", respostaJSON$current$precipitation_probability, "%"
)

print(horas)
print(temperatura)
print(umidade_rel)
print(chance_chuva)


# install.packages("httr")
# install.packages("jsonlite")