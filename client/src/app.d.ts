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

	interface ImageData{
		name: string;
		ext: string;
		result: string;
		created_at: string;
		username: string;
		status: string;
	}

	interface HistoryResponse{
		imageDatas: ImageData[];
	}

	interface UpdateImageDataResponse{
		imageData?: ImageData;
		error?: string;
	}
}

export {};
