
<template>
  <div>
    <h2>Sistema de Cadastro de Pessoas</h2>

    <!-- Formulário de Cadastro de Pessoa -->
    <PessoaForm ref="pessoaForm" @cadastro-sucesso="fetchPessoas" @editar-sucesso="fetchPessoas" @resetar-form="resetarPessoaEditando" />

    <!-- Exibir Lista de Pessoas Cadastradas -->
    <h3>Pessoas Cadastradas</h3>
    <PessoaList :pessoas="pessoas" @pessoa-deletada="fetchPessoas" @editar-pessoa="editarPessoa" />

    <!-- Exibir o peso ideal da pessoa -->
    <div v-if="pessoaEditando">
      <h4>Peso Ideal: {{ calcularPesoIdeal(pessoaEditando) }}</h4>
      <!-- Botão Voltar - Só aparece quando está editando uma pessoa -->
      <button @click="voltarParaCadastro" class="bg-gray-500 text-white py-2 px-4 rounded mt-4">Voltar</button>
    </div>
  </div>
</template>

<script>
import PessoaForm from './PessoaForm.vue'
import PessoaList from './PessoaList.vue'
import axios from 'axios'

export default {
  components: {
    PessoaForm,
    PessoaList
  },
  data() {
    return {
      pessoas: [],
      pessoaEditando: null
    }
  },
  mounted() {
    this.fetchPessoas()  // Carrega a lista de pessoas quando a página é carregada
  },
  methods: {
    // Método para obter todas as pessoas cadastradas
    async fetchPessoas() {
      try {
        const response = await axios.get('http://localhost:8000/api/pessoas/')
        this.pessoas = response.data
      } catch (error) {
        console.error('Erro ao carregar pessoas:', error)
      }
    },

    // Método para editar pessoa (caso precise)
    editarPessoa(pessoa) {
      this.pessoaEditando = pessoa
      // Passa os dados da pessoa para o formulário de edição
      this.$refs.pessoaForm.pessoa = { ...pessoa }
    },

    // Função para calcular o peso ideal com base no sexo e altura
    calcularPesoIdeal(pessoa) {
      let pesoIdeal = 0
      if (pessoa.sexo === 'm') {
        pesoIdeal = (72.7 * pessoa.altura) - 58
      } else if (pessoa.sexo === 'f') {
        pesoIdeal = (62.1 * pessoa.altura) - 44.7
      }
      return pesoIdeal.toFixed(2) // Retorna o peso ideal com 2 casas decimais
    },

    // Resetar a pessoa sendo editada
    resetarPessoaEditando() {
      this.pessoaEditando = null
    },

    // Método para voltar para a tela de cadastro de pessoa
    voltarParaCadastro() {
      this.pessoaEditando = null
      this.$refs.pessoaForm.resetForm()
    }
  }
}
</script>
