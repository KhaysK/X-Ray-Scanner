<script lang="ts">
	import { goto } from "$app/navigation";
	import { onMount } from "svelte";
	import { clearUser } from "../../apis";
    
    onMount(()=>{
        clearUser();
        goto('/');
    })


</script>