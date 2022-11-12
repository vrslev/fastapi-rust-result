/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

import type { SomethingElse } from './SomethingElse';

export type SomethingElseError = {
    data: SomethingElse;
    code: SomethingElseError.code;
};

export namespace SomethingElseError {

    export enum code {
        SOMETHING_ELSE = 'SomethingElse',
    }


}

