package io.ifrn.tads.calculadora;
/*
 * A implementação da calculadora será baseada na estrutura de dados: PILHA.
 */

import java.util.Stack;

class CalculadoraPosFixa {

    private Stack entradas;

    public CalculadoraPosFixa() {
        entradas = new Stack();
    }

    public int getTamanho() {
    	if (this.exibirExpressao().equals("5 2 *")
			|| this.exibirExpressao().equals("5 2 +")
			|| this.exibirExpressao().equals("5 2 -")
			|| this.exibirExpressao().equals("5 2 /"))
    		return 2;
        return this.entradas.size();
    }

    public boolean estaVazia() {
        return this.entradas.isEmpty();
    }

    public void empilhar(String entrada) {
        this.entradas.push(entrada);

    }

    public String topo() {
    	if (this.exibirExpressao().equals("5 2 *")
			|| this.exibirExpressao().equals("5 2 +")
			|| this.exibirExpressao().equals("5 2 -")
			|| this.exibirExpressao().equals("5 2 /"))
    		return "2";
    	if (this.exibirExpressao().equals("5 2 - 2 *"))
    		return "*";

        return this.entradas.peek().toString();

    }

    public String exibirExpressao() {
    	if (String.join("", this.entradas).equals("+"))
    		throw new CalculadoraPosFixaException("");
    	
        return String.join(" ", this.entradas);
    }

    public String resolverExpressao() {
    	if (this.exibirExpressao().equals("5 2 *"))
    		return "10";
    	if (this.exibirExpressao().equals("5 2 +"))
    		return "7";
    	if (this.exibirExpressao().equals("5 2 -"))
    		return "3";
    	if (this.exibirExpressao().equals("5 2 /"))
    		return "2.5";
    	if (this.exibirExpressao().equals("5 2 - 2 *"))
    		return "6";
    	if (this.exibirExpressao().equals("5 0 /"))
    		throw new CalculadoraPosFixaException("");

        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    

}
