export function useApi() {
    const conf = useRuntimeConfig();
    return conf.public.apiurl;
}