/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { Err_InvalidCredentials_ } from '../models/Err_InvalidCredentials_';
import type { Ok_User_ } from '../models/Ok_User_';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class DefaultService {

    /**
     * Me
     * @param returnOk
     * @returns any Successful Response
     * @throws ApiError
     */
    public static meMeGet(
        returnOk: boolean,
    ): CancelablePromise<(Ok_User_ | Err_InvalidCredentials_)> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/me',
            query: {
                'return_ok': returnOk,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

}
