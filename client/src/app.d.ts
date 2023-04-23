// See https://kit.svelte.dev/docs/types#app
// for information about these interfaces
declare global {
	
	interface User{
		username: string;
	}

	interface PredictionResult{
		result?: string;
		error?: string;
	}

	interface LoginResponse{
		username?: string;
		error?: string;
	}

	interface RegisterResponse{
		username?: string;
		error?: string;
	}
}

export {};
