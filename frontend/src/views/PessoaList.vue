<template>
  <div>
    <div>
      <!-- Campo de pesquisa -->
      <input 
        type="text" 
        v-model="pesquisa" 
        placeholder="Pesquisar por nome..." 
        class="w-full p-2 border rounded mb-4"
      />
      <button @click="pesquisar" class="w-full bg-blue-500 text-white py-2 rounded hover:bg-blue-600">Pesquisar</button>
    </div>

    <ul>
      <li v-for="pessoa in pessoasFiltradas" :key="pessoa.id" class="mb-4">
        <div>
          <!-- Exibir os dados da pessoa -->
          <span><strong>Nome:</strong> {{ pessoa.nome }}</span><br/>
          <span><strong>Data de Nascimento:</strong> {{ pessoa.data_nasc }}</span><br/>
          <span><strong>CPF:</strong> {{ pessoa.cpf }}</span><br/>
          <span><strong>Sexo:</strong> {{ pessoa.sexo === 'm' ? 'Masculino' : 'Feminino' }}</span><br/>
          <span><strong>Altura:</strong> {{ pessoa.altura }} m</span><br/>
          <span><strong>Peso:</strong> {{ pessoa.peso }} kg</span><br/>
        </div>

        <!-- Botões para editar ou deletar -->
        <div class="mt-2">
          <button @click="editPessoa(pessoa)" class="bg-yellow-500 text-white py-2 px-4 rounded hover:bg-yellow-600">Editar</button>
          <button @click="deletePessoa(pessoa.id)" class="bg-red-500 text-white py-2 px-4 rounded hover:bg-red-600">Deletar</button>
          <!-- Exibir o botão voltar se estiver editando -->
          <button v-if="pessoaEditando && pessoaEditando.id === pessoa.id" @click="voltarEdicao" class="bg-gray-500 text-white py-2 px-4 rounded hover:bg-gray-600">Voltar</button>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  props: {
    pessoas: Array,
    pessoaEditando: Object
  },
  data() {
    return {
      pesquisa: '', // Campo para armazenar o nome da pesquisa
    }
  },
  computed: {
    // Filtra a lista de pessoas com base na pesquisa
    pessoasFiltradas() {
      if (this.pesquisa === '') {
        return this.pessoas
      }
      return this.pessoas.filter(pessoa =>
        pessoa.nome.toLowerCase().includes(this.pesquisa.toLowerCase())
      )
    }
  },
  methods: {
    // Método para deletar pessoa
    async deletePessoa(id) {
      try {
        const response = await axios.delete(`http://localhost:8000/api/pessoas/${id}/`)
        if (response.status === 204) {
          this.$emit('pessoa-deletada', id)
        }
      } catch (error) {
        console.error('Erro ao deletar pessoa:', error)
        alert('Erro ao deletar pessoa.')
      }
    },

    // Método para editar pessoa
    editPessoa(pessoa) {
      this.$emit('editar-pessoa', pessoa)
    },

    // Método para voltar à tela de cadastro
    voltarEdicao() {
      this.$emit('resetar-form')
    },

    // Método de pesquisa
    pesquisar() {
      // Apenas para garantir que a pesquisa seja acionada corretamente
      this.pesquisa = this.pesquisa.trim()
    }
  }
}
</script>

