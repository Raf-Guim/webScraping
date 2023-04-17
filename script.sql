
-- -----------------------------------------------------
-- Schema webScraping
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS webScraping DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE webScraping ;

-- -----------------------------------------------------
-- Table colecao
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS colecao (
    id INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    PRIMARY KEY (id),
    UNIQUE INDEX id_UNIQUE (id ASC) VISIBLE,
    UNIQUE INDEX nome_UNIQUE (nome ASC) VISIBLE);


-- -----------------------------------------------------
-- Table relatorioDiario
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS relatorioDiario (
    id INT NOT NULL AUTO_INCREMENT,
    posicao INT NOT NULL,
    colecao_nome VARCHAR(100) NOT NULL,
    volume INT NOT NULL,
    variacao FLOAT NOT NULL,
    preco DECIMAL(9,2) NOT NULL,
    vendas INT NOT NULL,
    donosUnicos INT NOT NULL,
    listagem FLOAT NOT NULL,
    dia DATE NOT NULL,
    colecao_id INT NOT NULL,

    PRIMARY KEY (id),
    UNIQUE INDEX id_UNIQUE (id ASC) VISIBLE,
    INDEX colecao_id_idx (colecao_id ASC) VISIBLE,
    CONSTRAINT colecao_id
    FOREIGN KEY (colecao_id)
    REFERENCES colecao (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
