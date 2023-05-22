import app = require("teem");

//**********************************************************************************
// Se por acaso ocorrer algum problema de conexão, autenticação com o MySQL,
// por favor, execute este código abaixo no MySQL e tente novamente!
//
// ALTER USER 'USUÁRIO'@'localhost' IDENTIFIED WITH mysql_native_password BY 'SENHA';
//
// * Assumindo que o usuário seja root e a senha root, o comando ficaria assim:
//
// ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'root';
//
//**********************************************************************************

class IndexRoute {
	public async index(req: app.Request, res: app.Response) {
		/*
		let dados: any[];

		await app.sql.connect(async (sql) => {

			// Todas os comandos SQL devem ser executados aqui dentro do app.sql.connect().

			dados = await sql.query("SELECT ...");

		});

		let opcoes = {
			dados: dados
		};
		*/

		let opcoes = {
			dados: []
		};

		res.render("index/index", opcoes);
	}

	public async sobre(req: app.Request, res: app.Response) {
		res.render("index/sobre");
	}
}

export = IndexRoute;
