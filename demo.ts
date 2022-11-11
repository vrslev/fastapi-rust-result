import { DefaultService } from "./ts-client/services/DefaultService";

class AppError<T> extends Error {
  value: T;

  constructor(value: T) {
    super();
    this.value = value;
  }
}

async function handling_error<F extends () => Promise<T>, T>(
  func: F
): Promise<Extract<Awaited<ReturnType<F>>, { error?: undefined }>> {
  const result = await func();

  // @ts-ignore
  if (result.data) {
    // @ts-ignore
    return result;
  }

  throw new AppError(result);
}

const ok = await handling_error(() => DefaultService.meMeGet(true));
