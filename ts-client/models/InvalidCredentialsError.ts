/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

import type { InvalidCredentials } from './InvalidCredentials';

export type InvalidCredentialsError = {
    data: InvalidCredentials;
    code: InvalidCredentialsError.code;
};

export namespace InvalidCredentialsError {

    export enum code {
        INVALID_CREDENTIALS = 'InvalidCredentials',
    }


}

