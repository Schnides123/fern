<?php

namespace Seed\V2\Problem;

use Seed\Core\SerializableType;
use Seed\Core\JsonProperty;

class TestCaseExpects extends SerializableType
{
    /**
     * @var ?string $expectedStdout
     */
    #[JsonProperty("expectedStdout")]
    public ?string $expectedStdout;

    /**
     * @param ?string $expectedStdout
     */
    public function __construct(
        ?string $expectedStdout = null,
    ) {
        $this->expectedStdout = $expectedStdout;
    }
}
