/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { User } from '../models/User';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class DefaultService {

    /**
     * Me
     * @param returnOk
     * @returns User Successful Response
     * @throws ApiError
     */
    public static meMeGet(
        returnOk: boolean,
    ): CancelablePromise<User> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/me',
            query: {
                'return_ok': returnOk,
            },
            errors: {
                400: `Bad Request`,
                422: `Validation Error`,
            },
        });
    }

}
