<template>
	<header class="py-4 w-full border-b fixed top-0 left-0 z-50 bg-white">
		<div class="mx-auto w-10/12 flex justify-between">
			<nuxt-link to="/" class="flex items-center"
				><img class="h-10" src="/logo.svg" alt="logo" />
				<p class="ml-2 text-lg text-slate-900 font-bold">
					тариф<span class="text-indigo-500">тренд</span>
				</p></nuxt-link
			>
			<nav class="w-1/2">
				<ul class="flex justify-end h-full items-center">
					<li class="mr-4 text-sm text-slate-900 hover:text-slate-500">
						<nuxt-link to="/">Главная</nuxt-link>
					</li>
					<!--          <li class="mr-4 text-sm text-slate-900 hover:text-slate-500">
            <nuxt-link to="/favorites">Избранное</nuxt-link>
          </li>-->

					<li>
						<nuxt-link to="/sravni"
							><button
								class="border-2 px-7 text-sm font-md py-2 bg-white rounded-3xl border-slate-400 text-slate-700 box-border hover:bg-indigo-500 hover:text-white transition-all h-10 hover:border-opacity-0"
							>
								Подобрать тариф
							</button></nuxt-link
						>
					</li>
					<li v-if="!user">
						<nuxt-link to="/login"
							><button
								class="ml-2 border-2 px-7 text-sm font-md py-2 bg-white rounded-3xl border-slate-400 text-slate-700 box-border hover:bg-indigo-500 hover:text-white transition-all h-10 hover:border-opacity-0"
							>
								Войти
							</button></nuxt-link
						>
					</li>
					<li v-else>
						<button
							@click="logout"
							class="ml-2 border-2 px-7 text-sm font-md py-2 bg-white rounded-3xl border-slate-400 text-slate-700 box-border hover:bg-indigo-500 hover:text-white transition-all h-10 hover:border-opacity-0"
						>
							Выйти, {{ user.username }}
						</button>
					</li>
				</ul>
			</nav>
		</div>
	</header>
</template>

<script setup>
import { useAuthStore } from '~/store/index'

const authStore = useAuthStore()
const user = computed(() => authStore.user)

const logout = () => {
	authStore.logout()
}
</script>
