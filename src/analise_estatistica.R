# Tamires Vitória Ferreira dos Santos — FIAP — Fase 1 — Cap 1
# FarmTech Solutions — análise estatística dos dados exportados pelo Python
# + consulta à API pública Open-Meteo (Ir Além)

# Instala os pacotes apenas se ainda não estiverem disponíveis
for (pacote in c("httr", "jsonlite")) {
  if (!requireNamespace(pacote, quietly = TRUE)) {
    install.packages(pacote, repos = "https://cloud.r-project.org")
  }
}

library(httr)
library(jsonlite)

# Localiza o CSV na mesma pasta do script (funciona com Rscript, source() e RStudio)
pasta_script <- tryCatch({
  arg <- grep("^--file=", commandArgs(trailingOnly = FALSE), value = TRUE)
  if (length(arg) > 0) {
    dirname(normalizePath(sub("^--file=", "", arg[1])))
  } else if (!is.null(sys.frames()[[1]]$ofile)) {
    dirname(normalizePath(sys.frames()[[1]]$ofile))
  } else {
    getwd()
  }
}, error = function(e) getwd())
arquivo_csv <- file.path(pasta_script, "farmtech_dados.csv")

if (!file.exists(arquivo_csv)) {
  stop("Arquivo farmtech_dados.csv não encontrado. Rode o farmtech.py e use a opção [5] para exportar.")
}

cat("=====================================================\n")
cat("  FARMTECH SOLUTIONS — Analise R\n")
cat("=====================================================\n\n")

cat("--- ANALISE ESTATISTICA DOS DADOS DA FAZENDA ---\n\n")

dados <- read.csv(arquivo_csv, stringsAsFactors = FALSE)

# Área cultivada
cat("AREA CULTIVADA (m2):\n")
cat(sprintf("  Media:         %.2f m2\n", mean(dados$area_m2)))
cat(sprintf("  Desvio padrao: %.2f m2\n", sd(dados$area_m2)))
cat(sprintf("  Minimo:        %.2f m2\n", min(dados$area_m2)))
cat(sprintf("  Maximo:        %.2f m2\n", max(dados$area_m2)))
cat(sprintf("  Total fazenda: %.2f m2\n\n", sum(dados$area_m2)))

# Insumo 1
cat("INSUMO 1 — totais por area (mL):\n")
cat(sprintf("  Media:         %.2f mL\n", mean(dados$total_ins1)))
cat(sprintf("  Desvio padrao: %.2f mL\n", sd(dados$total_ins1)))
cat(sprintf("  Minimo:        %.2f mL\n", min(dados$total_ins1)))
cat(sprintf("  Maximo:        %.2f mL\n", max(dados$total_ins1)))
cat(sprintf("  Total geral:   %.2f mL\n\n", sum(dados$total_ins1)))

# Insumo 2
cat("INSUMO 2 — totais por area (mL):\n")
cat(sprintf("  Media:         %.2f mL\n", mean(dados$total_ins2)))
cat(sprintf("  Desvio padrao: %.2f mL\n", sd(dados$total_ins2)))
cat(sprintf("  Minimo:        %.2f mL\n", min(dados$total_ins2)))
cat(sprintf("  Maximo:        %.2f mL\n", max(dados$total_ins2)))
cat(sprintf("  Total geral:   %.2f mL\n\n", sum(dados$total_ins2)))

# Detalhamento por área
cat("DETALHAMENTO POR AREA:\n")
for (i in 1:nrow(dados)) {
  cat(sprintf("  Area %s | %s | %s\n",
              dados$area[i], dados$cultura[i], dados$figura[i]))
  cat(sprintf("    Area cultivada: %.2f m2\n", dados$area_m2[i]))
  cat(sprintf("    %s: dose %.2f mL/m2 -> total %.2f mL\n",
              dados$insumo1[i], dados$dose_ins1[i], dados$total_ins1[i]))
  cat(sprintf("    %s: dose %.2f mL/m2 -> total %.2f mL\n\n",
              dados$insumo2[i], dados$dose_ins2[i], dados$total_ins2[i]))
}

cat("=====================================================\n")
cat("--- DADOS METEOROLOGICOS — Joao Pessoa / PB ---\n\n")

# Monta a URL com as coordenadas de João Pessoa
url <- paste0(
  "https://api.open-meteo.com/v1/forecast",
  "?latitude=-7.12&longitude=-34.86",
  "&current=temperature_2m,relative_humidity_2m,precipitation,wind_speed_10m",
  "&wind_speed_unit=kmh&timezone=America/Recife"
)

# Chama a API e converte a resposta (sem derrubar a análise se a internet falhar)
clima <- tryCatch({
  resposta <- GET(url, timeout(15))
  stop_for_status(resposta)
  fromJSON(content(resposta, as = "text", encoding = "UTF-8"))
}, error = function(e) NULL)

if (is.null(clima)) {
  cat("  Nao foi possivel consultar a API de clima agora (sem conexao?).\n")
} else {
  # Exibe os dados climáticos atuais
  cat(sprintf("  Temperatura:  %.1f graus C\n", clima$current$temperature_2m))
  cat(sprintf("  Umidade:      %.0f %%\n",      clima$current$relative_humidity_2m))
  cat(sprintf("  Precipitacao: %.1f mm\n",      clima$current$precipitation))
  cat(sprintf("  Vento:        %.1f km/h\n",    clima$current$wind_speed_10m))
}

cat("\n=====================================================\n")
cat("  Analise concluida — FarmTech Solutions\n")
cat("=====================================================\n")