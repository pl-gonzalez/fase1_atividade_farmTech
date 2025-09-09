library(httr)
library(jsonlite)

url <- paste0(
  "https://api.open-meteo.com/v1/forecast?latitude=",-23.5489,"&longitude=",-46.6388,"&timezone=America%2FSao_Paulo&current=temperature_2m,relative_humidity_2m,precipitation_probability,rain,cloud_cover_mid,wind_speed_10m,temperature_80m,apparent_temperature&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"

)

# Requisição para a API
resposta <- httr :: GET(url)

resposta_content <- httr :: content(resposta, as = "text")

respostaJSON = jsonlite::fromJSON(resposta_content)



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